import yaml
import re
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.db import models
from datetime import datetime, date
from django.utils import timezone

class Command(BaseCommand):
    help = "Import a database from a yaml file"

    def get_sorted_tables_list(self, data):

        sorted = []
        tables = {}

        # first get all tables, unsorted
        for modulename in data:
            if modulename == "Sequences":
                continue
            for tablename in data[modulename]:
                classname = tablename[:-len('Table')]
                if classname == 'ACostCentreTypes':
                    classname = 'ACostCentreType'
                model = apps.get_model('data', classname)
                referencedTables = []
                for field in model._meta.get_fields():
                    if "_" in field.name:
                        continue
                    try:
                        if field.is_relation:
                            if field.related_model.__name__ != classname:
                                referencedTables.append(field.related_model.__name__)
                    except:
                        None
                if len(referencedTables) == 0:
                    sorted.append(classname)
                else:
                    tables[classname] = referencedTables

        while len(tables.keys()) > 0:
            foundAny = False
            for tablename in tables:
                allAvailable = True
                for referencedTable in tables[tablename]:
                    if not referencedTable in sorted:
                        allAvailable = False
                if allAvailable:
                    sorted.append(tablename)
                    del(tables[tablename])
                    foundAny = True
                    break
            if not foundAny:
                print(tables.keys())
                raise Exception("get_sorted_tables_list: there are still tables left")

        return sorted


    def find_compositekey(self, model: models.Model):

        # try the unique constraint with postfix _pk (from petra.xml)
        for constr in model._meta.constraints:
            if constr.name.endswith('_pk'):
                return constr.fields

        # try the first field, if it is unique
        for f in model._meta.get_fields():
            if f.name != 'id':
                try:
                    if f.unique:
                        return [f.name]
                    break
                except:
                    None

    def drop_prefix(self, tablename):
        return tablename[[ match.start() for match in re.finditer ("[A-Z]", tablename) ][1]:]

    def get_modulename(self, data, tablename):
        for modulename in data:
            for table in data[modulename]:
                if table == tablename:
                    return modulename
        raise Exception(f"cannot find module for {tablename}")

    def import_table(self, data, tablename):

        tabledata = None
        if tablename == 'ACostCentreTypeTable':
            modulename = self.get_modulename(data, 'ACostCentreTypesTable')
            tabledata = data[modulename]['ACostCentreTypesTable']
        else:
            modulename = self.get_modulename(data, tablename)
            tabledata = data[modulename][tablename]

        if tabledata is None:
            return

        print(f"importing table {tablename}")
        classname = tablename[:-len('Table')]

        for row in tabledata:
            model = apps.get_model('data', classname)
            # print(model)
            values = tabledata[row]
            # print(values)

            insert = {}
            fields_of_composite_keys = []
            missing_fields = []
            for name in values:
                # for PBankingTypeTable, we ignore the id column
                if name in ['Id']:
                    continue
                # for AAccountHierarchyDetail, we ignore ALedgerNumber
                if classname == "AAccountHierarchyDetail" and name == "LedgerNumber":
                    continue
                # TODO
                if name in ['DateCreated', 'CreatedBy', 'DateModified', 'ModifiedBy']:
                    continue
                field = None
                droppedSuffix = None
                try:
                    field = model._meta.get_field(name)
                except:
                    None

                if classname == "PRecentPartnersTable" and name == "When":
                    field = model._meta.get_field('WhenDate')
                if classname == "PRecentPartnersTable" and name == "WhenT":
                    field = model._meta.get_field('WhenTime')

                if field is None and name.endswith('Code'):
                    try:
                        field = model._meta.get_field(name.replace('Code', ''))
                        droppedSuffix = 'Code'
                    except:
                        None
                if field is None and name.endswith('Id'):
                    try:
                        field = model._meta.get_field(name.replace('Id', ''))
                        droppedSuffix = 'Id'
                    except:
                        None
                if field is None and name.endswith('Key'):
                    try:
                        field = model._meta.get_field(name.replace('Key', ''))
                        droppedSuffix = 'Key'
                    except:
                        None
                if field is None and name.endswith('Number'):
                    try:
                        field = model._meta.get_field(name.replace('Number', ''))
                        droppedSuffix = 'Number'
                    except:
                        None
                if field is None and name.endswith('Flag'):
                    try:
                        # eg. AAccount.UseForeignCurrency
                        field = model._meta.get_field('Use' + name.replace('Flag', ''))
                        droppedSuffix = 'Flag'
                    except:
                        None
                if field is None and name.endswith('Flag'):
                    try:
                        field = model._meta.get_field(name.replace('Flag', ''))
                        droppedSuffix = 'Flag'
                    except:
                        None
                if field is None:
                    tablenameWithoutPrefix = self.drop_prefix(classname)
                    if name.startswith(tablenameWithoutPrefix) and (
                        name.endswith('Code') or name.endswith('Name') or name.endswith('Key') or name.endswith('Desc') or name.endswith('Descr')):
                        try:
                            field = model._meta.get_field(name[len(tablenameWithoutPrefix):])
                        except:
                            None

                if field is None:
                    missing_fields.append(name)
                    continue

                if field.is_relation:
                    print(f"    foreign key: field {field.name} => {field.related_model.__name__}")
                    compositekey = self.find_compositekey(field.related_model)
                    filter = {}
                    for f in compositekey:
                        importedfield = f
                        print("        " + f)
                        if not importedfield in values:
                            # eg. prefix Code with referenced Table name
                            importedfield = self.drop_prefix(field.related_model.__name__) + f
                        if not importedfield in values and len(compositekey) == 1:
                            # eg. PRelation.RelationCategory
                            importedfield = self.drop_prefix(field.related_model.__name__)
                        if not importedfield in values and len(compositekey) == 1:
                            # eg. PType.Category
                            importedfield = field.name
                        if not importedfield in values and len(compositekey) == 1:
                            # eg. PUnit.Partner
                            importedfield = field.name + droppedSuffix
                        if not importedfield in values and field.null == True:
                            # this is allowed to be null
                            continue
                        if not importedfield in values and f == 'Ledger':
                            importedfield = "LedgerNumber"
                        if not importedfield in values and classname == "AAccountHierarchy" and f == 'Code':
                            importedfield = "RootAccountCode"
                        #if not importedfield in values and classname == "AAccountHierarchyDetail" and field.name == 'ReportingAccountCode':
                        #    importedfield = field.name
                        #if not importedfield in values and classname == "AAccountHierarchyDetail" and field.name == 'AccountCodeToReportTo':
                        #    importedfield = field.name
                        if not importedfield in values and field.name in values:
                            importedfield = field.name
                        filter_on_field = f
                        otherfield = field.related_model._meta.get_field(f)
                        if otherfield.is_relation:
                            #eg. PPartnerLedgerTable.Partner => PUnit
                            if otherfield.name == 'Partner':
                                filter_on_field = f'{f}__Key'
                            elif otherfield.name == 'Ledger':
                                filter_on_field = f'{f}__LedgerNumber'

                        filter[filter_on_field] = values[importedfield]
                        fields_of_composite_keys.append(importedfield)
                    if len(filter.keys()) > 0:
                        print(f"      filter: {filter}")
                        refobj = field.related_model.objects.get(**filter)
                        print(f"       result: {refobj}")
                        insert[field.name] = refobj
                else:
                    value = values[name]
                    if isinstance(value, date):
                        value = datetime(value.year, value.month, value.day, tzinfo=timezone.get_default_timezone())
                    elif isinstance(value, str) and len(value) == len('YYYY-MM-DD hh:mm:ss'):
                        f = model._meta.get_field(field.name)
                        if type(f) is models.DateTimeField:
                            value = datetime(int(value[0:4]), int(value[5:7]), int(value[8:10]),
                                                int(value[11:13]), int(value[14:16]), int(value[17:19]),
                                                tzinfo=timezone.get_default_timezone())
                    insert[field.name] = value

            for fieldname in missing_fields:
                # ignore fields that are already part of a composite key
                if fieldname in fields_of_composite_keys:
                    continue

                raise Exception(f"cannot find field {fieldname}")

            obj = model.objects.create(**insert)


    def import_database(self, data):

        # get tables in order for import
        tables = self.get_sorted_tables_list(data)

        for tablename in tables:
            self.import_table(data, f"{tablename}Table")

        # TODO
        # print("Sequences")
        # for sequence in data["Sequences"]:
        #    print(f"  {sequence}")



    def handle(self, *args, **options):
        # TODO: use parameter
        with open("definitions/clean.yml") as stream:
            try:
                data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return

        if data is not None:
            self.import_database(data['RootNodeInternal'])
