import yaml
import re
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.db import models
from datetime import datetime, date
from django.utils import timezone
from django.contrib.auth.models import User, Group

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

        # PBankingType
        if model.__name__ == 'PBankingType':
            f = model._meta.get_field('OldId')
            return [f.name]

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

    def fix_date(self, value):
        return datetime(value.year, value.month, value.day, tzinfo=timezone.get_default_timezone())

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
                # for PBankingDetailsUsage, we ignore PartnerKey
                if classname == "PBankingDetailsUsage" and name == "PartnerKey":
                    continue
                # for PPartnerGiftDestination, we ignore Key
                if classname == "PPartnerGiftDestination" and name == "Key":
                    continue
                # for AJournal, we ignore SubSystem
                if classname == "AJournal" and name == "SubSystemCode":
                    continue
                # for AProcessedFee, we ignore GiftTransactionNumber
                if classname == "AProcessedFee" and name == "GiftTransactionNumber":
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

                # for PBankingTypeTable, we must rename this column
                if name == "Id":
                    field = model._meta.get_field('OldId')

                if field is None and classname == "PRecentPartners":
                    if name == "When":
                        field = model._meta.get_field('WhenDate')
                    elif name == "WhenT":
                        field = model._meta.get_field('WhenTime')

                if field is None and classname == "MExtractMaster":
                    if name == "ManualMod":
                        field = model._meta.get_field('ManualModification')
                    elif name == "ManualModT":
                        field = model._meta.get_field('ManualModificationDate')

                if field is None and classname == "AAccountHierarchyDetail":
                    if name == "AccountCodeToReportTo":
                        field = model._meta.get_field('AccountToReportTo')
                    elif name == "ReportingAccountCode":
                        field = model._meta.get_field('ReportingAccount')

                if field is None and classname == "ATransactionType":
                    if name == "DebitAccountCode":
                        field = model._meta.get_field('DebitAccount')
                    elif name == "CreditAccountCode":
                        field = model._meta.get_field('CreditAccount')

                if field is None and classname == "PBankingDetailsUsage":
                    if name == "BankingDetailsKey":
                        field = model._meta.get_field('PartnerBankingDetails')

                if field is None and classname in ("AGift", "AGiftDetail", "AProcessedFee"):
                    if name == "BatchNumber":
                        field = model._meta.get_field('GiftBatch')

                if field is None and classname in ["ARecurringGift", "ARecurringGiftDetail"]:
                    if name == "BatchNumber":
                        field = model._meta.get_field('RecurringGiftBatch')

                if field is None and classname in ("AProcessedFee"):
                    if name == "DetailNumber":
                        field = model._meta.get_field('GiftDetail')
                    if name == "PeriodNumber":
                        field = model._meta.get_field('AccountingPeriod')

                if field is None and classname == "AGiftDetail":
                    if name == "GiftTransactionNumber":
                        field = model._meta.get_field('Gift')

                if field is None and classname == "ARecurringGiftDetail":
                    if name == "GiftTransactionNumber":
                        field = model._meta.get_field('RecurringGift')

                if field is None and classname == "AApDocument":
                    if name == "ApDocumentId":
                        field = model._meta.get_field('id')

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
                if field is None and name.endswith('Name'):
                    try:
                        field = model._meta.get_field(name.replace('Name', ''))
                        droppedSuffix = 'Name'
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

                #if self.DEBUG:
                #    print(f"    field: {field.name} is_relation: {field.is_relation}")

                if field.is_relation and field.related_model.__name__ == 'AApDocument':
                    if self.DEBUG:
                        print(f"    foreign key: field {field.name} => {field.related_model.__name__}")
                        print(f"        id")
                    filter = {}
                    filter['id'] = values['ApDocumentId']
                    if self.DEBUG:
                        print(f"      filter: {filter}")
                    refobj = field.related_model.objects.get(**filter)
                    if self.DEBUG:
                        print(f"       result: {refobj}")
                    insert[field.name] = refobj

                elif field.is_relation:
                    if self.DEBUG:
                        print(f"    foreign key: field {field.name} => {field.related_model.__name__}")

                    compositekey = self.find_compositekey(field.related_model)
                    filter = {}
                    for f in compositekey:
                        importedfield = f
                        if self.DEBUG:
                            print(f"        {f}")
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
                        if not importedfield in values and classname == "AAccountHierarchy" and f == 'Code':
                            importedfield = "RootAccountCode"
                        if not importedfield in values and classname == "AAccountHierarchyDetail" and field.name == 'ReportingAccount':
                            importedfield = "ReportingAccountCode"
                        if not importedfield in values and classname == "AAccountHierarchyDetail" and field.name == 'AccountToReportTo':
                            importedfield = "AccountCodeToReportTo"
                        if not importedfield in values and classname == "ATransactionType" and field.name == 'DebitAccount':
                            importedfield = "DebitAccountCode"
                        if not importedfield in values and classname == "ATransactionType" and field.name == 'CreditAccount':
                            importedfield = "CreditAccountCode"
                        if not importedfield in values and classname == "AEpStatement" and field.name == 'BankAccount':
                            importedfield = "BankAccountCode"
                        if not importedfield in values and classname == "PBankingDetailsUsage" and f == 'Partner':
                            importedfield = "PartnerKey"
                        if not importedfield in values and classname == "PBankingDetailsUsage" and f == 'BankingDetails':
                            importedfield = "BankingDetailsKey"
                        if not importedfield in values and classname == "AJournal" and f == 'TransactionType':
                            importedfield = "TransactionType"
                        if not importedfield in values and classname == "AJournal" and f == 'SubSystem':
                            importedfield = "SubSystemCode"
                        if not importedfield in values and classname == "ATransaction" and f == 'Batch':
                            importedfield = "BatchNumber"
                        if not importedfield in values and classname == "ATransaction" and f == 'Journal':
                            importedfield = "JournalNumber"
                        if not importedfield in values and classname == "AGiftBatch" and field.name == 'BankAccount':
                            importedfield = "BankAccountCode"
                        if not importedfield in values and classname == "AGiftBatch" and field.name == 'BankCostCentre':
                            importedfield = "BankCostCentreCode"
                        if not importedfield in values and classname == "AGiftDetail" and f == 'MotivationGroup':
                            importedfield = "MotivationGroupCode"
                        if not importedfield in values and classname == "AGiftDetail" and f == 'GiftBatch':
                            importedfield = "BatchNumber"
                        if not importedfield in values and classname == "AProcessedFee" and field.name == 'GiftDetail':
                            importedfield = "DetailNumber"
                        if not importedfield in values and classname == "AProcessedFee" and field.name == 'AccountingPeriod':
                            importedfield = "PeriodNumber"
                        if not importedfield in values and classname == "AMotivationDetailFee" and f == 'MotivationGroup':
                            importedfield = "MotivationGroupCode"
                        if not importedfield in values and classname == "AEpMatch" and f == 'MotivationGroup':
                            importedfield = "MotivationGroupCode"
                        if not importedfield in values and classname == "ARecurringGiftDetail" and f == 'MotivationGroup':
                            importedfield = "MotivationGroupCode"

                        if f == 'Ledger':
                            importedfield = "LedgerNumber"
                        elif classname == "PPartnerGiftDestination" and importedfield == "Key":
                            importedfield = field.name + "Key"
                        elif classname == "ARecurringGiftBatch" and field.name == 'BankAccount':
                            importedfield = "BankAccountCode"
                        elif classname == "ARecurringGiftBatch" and field.name == 'BankCostCentre':
                            importedfield = "BankCostCentre"
                        elif classname == "ARecurringGift" and field.name == 'RecurringGiftBatch':
                            importedfield = "BatchNumber"
                        elif classname == "ARecurringGiftDetail" and field.name == 'RecurringGiftBatch':
                            importedfield = "BatchNumber"
                        elif classname == "ARecurringGiftDetail" and field.name == 'RecurringGift':
                            importedfield = "GiftTransactionNumber"

                        if not importedfield in values and field.null == True:
                            # this is allowed to be null
                            continue

                        if not importedfield in values and field.name in values:
                            importedfield = field.name

                        # print(f"        importedfield: {importedfield}, classname: {classname}, field.name: {field.name}, f: {f}")
                        filter_on_field = f
                        otherfield = field.related_model._meta.get_field(f)
                        if otherfield.is_relation:
                            #eg. PPartnerLedgerTable.Partner => PUnit
                            if otherfield.name == 'Partner':
                                filter_on_field = f'{f}__Key'
                            elif otherfield.name == 'Ledger':
                                filter_on_field = f'{f}__LedgerNumber'
                            elif otherfield.name == 'SubSystem':
                                filter_on_field = f'{f}__Code'
                            elif otherfield.name == 'Batch':
                                filter_on_field = f'{f}__BatchNumber'
                            elif otherfield.name == 'Journal':
                                filter_on_field = f'{f}__JournalNumber'
                            elif otherfield.name == 'PositionScope':
                                filter_on_field = f'{f}__Code'
                            elif otherfield.name == 'MotivationGroup':
                                filter_on_field = f'{f}__Code'
                                # also filter on ledger number
                                filter['MotivationGroup__Ledger__LedgerNumber'] = values['LedgerNumber']
                            elif otherfield.name == 'Gift':
                                filter_on_field = f'Gift__GiftTransactionNumber'
                                # also filter on ledger number
                                filter['Gift__Ledger__LedgerNumber'] = values['LedgerNumber']
                                # also filter on batch number
                                filter['GiftBatch__BatchNumber'] = values['BatchNumber']
                            elif otherfield.name == 'RecurringGift':
                                filter_on_field = None
                                filter['GiftTransactionNumber'] = values['GiftTransactionNumber']
                                # also filter on ledger number
                                filter['RecurringGift__Ledger__LedgerNumber'] = values['LedgerNumber']
                            elif otherfield.name == 'RecurringGiftBatch':
                                filter_on_field = None
                                filter['RecurringGiftBatch__BatchNumber'] = values['BatchNumber']
                                # also filter on ledger number
                                filter['RecurringGiftBatch__Ledger__LedgerNumber'] = values['LedgerNumber']

                        if importedfield == "MotivationDetailCode":
                            # also filter on ledger number
                            filter['MotivationGroup__Ledger__LedgerNumber'] = values['LedgerNumber']
                            # also filter on motivation group
                            filter['MotivationGroup__Code'] = values['MotivationGroupCode']

                        if filter_on_field is not None:
                            filter[filter_on_field] = values[importedfield]
                        fields_of_composite_keys.append(importedfield)
                    if len(filter.keys()) > 0:
                        if self.DEBUG:
                            print(f"      filter: {filter}")
                        refobj = field.related_model.objects.get(**filter)
                        if self.DEBUG:
                            print(f"       result: {refobj}")
                        insert[field.name] = refobj
                else:
                    value = values[name]
                    if isinstance(value, date):
                        value = self.fix_date(value)
                    elif isinstance(value, str) and len(value) == len('YYYY-MM-DD hh:mm:ss'):
                        f = model._meta.get_field(field.name)
                        if type(f) is models.DateTimeField:
                            value = datetime(int(value[0:4]), int(value[5:7]), int(value[8:10]),
                                                int(value[11:13]), int(value[14:16]), int(value[17:19]),
                                                tzinfo=timezone.get_default_timezone())
                    if classname == "ACostCentre" and field.name == "Name" and value is None:
                        value = "N/A"
                    if classname == "PPartnerAttribute" and field.name == "Value" and value is None:
                        value = "N/A"
                    if classname == "ATransaction" and field.name == "Reference" and value is None:
                        value = "N/A"
                    if classname == "AEpMatch" and field.name == "Action" and value is None:
                        value = "UNMATCHED"
                    insert[field.name] = value

            for fieldname in missing_fields:
                # ignore fields that are already part of a composite key
                if fieldname in fields_of_composite_keys:
                    continue

                raise Exception(f"cannot find field {fieldname}")

            obj = model.objects.create(**insert)


    def import_database(self, data, startattable):

        # get tables in order for import
        tables = self.get_sorted_tables_list(data)

        ignore = False
        if startattable is not None:
            ignore = True
        for tablename in tables:
            if startattable is not None and startattable in [tablename, f"{tablename}Table"]:
                ignore = False
            if ignore:
                continue
            self.import_table(data, f"{tablename}Table")

        # TODO
        # print("Sequences")
        # for sequence in data["Sequences"]:
        #    print(f"  {sequence}")

    def import_auth(self, data):

        tabledata = data["MSysMan"]["SModuleTable"]
        for row, values in tabledata.items():
            Group.objects.get_or_create(name=values['ModuleId'])

        tabledata = data["MSysMan"]["SUserTable"]
        for row, values in tabledata.items():
            print(
                values['UserId'],
                values['EmailAddress'] if 'EmailAddress' in values else None,
                values['FirstName'] if 'FirstName' in values else None,
                values['LastName'] if 'LastName' in values else None,
                values['LastLoginDate'] if 'LastLoginDate' in values else None,
                values['Retired'] if 'Retired' in values else None,
                values['DateCreated'] if 'DateCreated' in values else None)
            user = User.objects.create_user(values['UserId'],
                values['EmailAddress'] if 'EmailAddress' in values else None)
            if 'LastLoginDate' in values:
                user.last_login = self.fix_date(values['LastLoginDate'])
            if 'DateCreated' in values:
                user.date_joined = self.fix_date(values['DateCreated'])
            if 'Retired' in values and values['Retired'] == True:
                user.is_active = False
            if 'AccountLocked' in values and values['AccountLocked'] == True:
                user.is_active = False
            if 'FirstName' in values:
                user.first_name = values['FirstName']
            if 'LastName' in values:
                user.last_name = values['LastName']
            user.save()

        tabledata = data["MSysMan"]["SUserModuleAccessPermissionTable"]
        for row, values in tabledata.items():
            if values['ModuleId'] == 'SYSMAN' and values['CanAccess'] == True:
                user = User.objects.get(username = values['UserId'])
                user.is_superuser = True
                user.is_staff = True
                user.save()
            if values['CanAccess'] == True:
                group = Group.objects.get(name = values['ModuleId'])
                user = User.objects.get(username = values['UserId'])
                user.groups.add(group)
                user.save()

    def add_arguments(self, parser):
        parser.add_argument(
            "--ymlfile",
            required=True,
            type=str,
            help = "The path to the file in yml format, that will be imported")
        parser.add_argument(
            "--debug",
            required=False,
            type=bool,
            default=False,
            help = "Should we print detailed messages during the import")
        parser.add_argument(
            "--startattable",
            required=False,
            type=str,
            help = "For Debugging: start import at this table")


    def handle(self, *args, **options):
        self.DEBUG = options['debug']
        with open(options["ymlfile"]) as stream:
            try:
                data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return

        if data is not None:
            self.import_database(data['RootNodeInternal'], options['startattable'])
            self.import_auth(data['RootNodeInternal'])
