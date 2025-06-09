from lxml import etree
from django.core.management.base import BaseCommand, CommandError
from functools import cmp_to_key
import copy

class Command(BaseCommand):
    help = "Creates the Django data model from the definition in petra.xml"

    def concat(self, list, separator=', '):
        s = ''
        for element in list:
            if element is not None and len(element) > 0:
                if len(s) > 0:
                    s += separator
                s += element
        return s

    def upper_camel_case(self, s, stripPrefix = False, stripSuffix = False, stripSuffixCodeOrKey = False, stripPrefixTableName = False, tableName = ''):
        if stripSuffix:
            if s.endswith('_flag_l'):
                s = s[:-1*len('_flag_l')] + '_l'

        if stripSuffixCodeOrKey:
            if s.endswith('_code_c'):
                s = s[:-1*len('_code_c')] + '_c'
            elif s.endswith('_key_n'):
                s = s[:-1*len('_key_n')] + '_n'
            elif s.endswith('_key_i'):
                s = s[:-1*len('_key_i')] + '_i'
            elif s.endswith('_id_c'):
                s = s[:-1*len('_id_c')] + '_c'
            elif s.endswith('_id_i'):
                s = s[:-1*len('_id_i')] + '_i'
            elif s.endswith('_name_c'):
                s = s[:-1*len('_name_c')] + '_c'
            elif s.endswith('_number_i'):
                s = s[:-1*len('_number_i')] + '_i'
        if stripPrefixTableName:
            if s.startswith(tableName) and (s.endswith('_code_c') or s.endswith('_name_c') or s.endswith('_descr_c') or s.endswith('_desc_c')):
                # keep prefix, but remove table name
                s = s[:s.index('_')] + s[len(tableName):]

        if stripPrefix and '_' in s:
            s = s[s.index('_')+1:]
        if stripSuffix and '_' in s:
            s = s[:s.rindex('_')]
        return s.replace('_', ' ').title().replace(" ", "")

    def process_field(self, f, tableName, className, fieldNode, primaryKeyNode, foreignKeyNodes):

        foreignkey = None
        if foreignKeyNodes is not None:
            for key in foreignKeyNodes:
                if key.attrib['thisFields'] == fieldNode.attrib['name']:
                    foreignkey = key

        fieldName = self.upper_camel_case(fieldNode.attrib['name'], stripPrefix=True, stripSuffix=True, stripPrefixTableName=True, tableName=tableName)
        fieldNode.attrib['fieldname'] = fieldName
        fieldType = fieldNode.attrib['type']

        if 'descr' in fieldNode.attrib and fieldNode.attrib['descr'].strip(' '):
            f.write(f"  # {fieldNode.attrib['descr'].strip()}\n")

        default = ''
        null = ''
        unique = ''

        if primaryKeyNode is not None and primaryKeyNode.attrib['thisFields'] == fieldNode.attrib['name']:
            unique = 'unique=True'

        if foreignkey is not None:
            fieldName = self.upper_camel_case(fieldNode.attrib['name'], stripPrefix=True, stripSuffix=True, stripSuffixCodeOrKey=True)
            fieldNode.attrib['fieldname'] = fieldName
            otherTable = self.upper_camel_case(foreignkey.attrib['otherTable'])
            if otherTable == className:
                otherTable = "'self'"
            #related_name = f'related_name="+"'
            related_name = f'related_name="{className}_{fieldName}"'

        if 'notnull' in fieldNode.attrib:
            if fieldNode.attrib['notnull'] == 'yes':
                null = 'null=False, blank=False'

        if foreignkey is not None:
                f.write(f"  {fieldName} = models.ForeignKey({self.concat([otherTable,default,null,related_name])}, on_delete=models.CASCADE)\n")
        elif fieldType == "varchar" or fieldType == "text":
            maxlength = 20
            if 'format' in fieldNode.attrib:
                format = fieldNode.attrib['format']
                if format.lower().startswith('x('):
                    maxlength = format[2:-1]
                elif format.lower().startswith('x('):
                    maxlength = len(format)

            if 'initial' in fieldNode.attrib:
                default = f"default='{fieldNode.attrib['initial']}'"

            max_length = f"max_length={maxlength}"
            f.write(f"  {fieldName} = models.CharField({self.concat([max_length,default,null,unique])})\n")
        elif fieldType == "bit":
            if 'initial' in fieldNode.attrib:
                if fieldNode.attrib['initial'].lower() == 'yes':
                    default = f"default=True"
                elif fieldNode.attrib['initial'].lower() == 'no':
                    default = f"default=False"
            f.write(f"  {fieldName} = models.BooleanField({self.concat([default,null])})\n")
        elif fieldType == "integer" or (fieldType == "number" and not 'decimals' in fieldNode.attrib):
            if 'initial' in fieldNode.attrib and fieldNode.attrib['initial'] != '?':
                default = f"default={fieldNode.attrib['initial']}"
            f.write(f"  {fieldName} = models.IntegerField({self.concat([default,null,unique])})\n")
        elif fieldType == "number" and 'decimals' in fieldNode.attrib:
            if 'initial' in fieldNode.attrib:
                default = f"default={fieldNode.attrib['initial']}"
            max_digits = f"max_digits={fieldNode.attrib['length']}"
            decimal_places = f"decimal_places={fieldNode.attrib['decimals']}"
            f.write(f"  {fieldName} = models.DecimalField({self.concat([max_digits, decimal_places, default,null])})\n")
        elif fieldType == "date" or fieldType == "datetime":
            f.write(f"  {fieldName} = models.DateTimeField({self.concat([null])})\n")

    def process_table(self, f, tableNode):
        print(f"process_table {tableNode.attrib['name']}")

        className = self.upper_camel_case(tableNode.attrib['name'])
        f.write(f'\n\nclass {className}(models.Model):\n')
        if len(tableNode.attrib["descr"]) > 0:
            f.write(f'  """\n  {tableNode.attrib["descr"]}\n  """\n\n')

        primarykey = None
        foreignkeys = []
        compositekeys = []
        uniquekeys = []
        fields = {}
        for child in tableNode:
            if child.tag == "primarykey":
                primarykey = child
                if ',' in primarykey.attrib['thisFields']:
                    uniquekeys.append(primarykey)
            if child.tag == "uniquekey":
                uniquekeys.append(child)
            if child.tag == "foreignkey":
                if "," in child.attrib['thisFields']:
                    compositekeys.append(child)
                else:
                    foreignkeys.append(child)
            if child.tag == "tablefield":
                child.attrib['dropped'] = "False"
                fields[child.attrib['name']] = child

        # replace composite foreign keys with direct foreign keys
        for key in compositekeys:

            fieldnames = key.attrib['thisFields'].replace(' ', '').split(',')
            first = True
            for fieldname in fieldnames:
                if first:
                    first = False
                    # create a new foreign key directly to the table
                    newfieldname = key.attrib['otherTable'] + "_x"
                    fields[newfieldname] = copy.deepcopy(fields[fieldname])
                    fields[newfieldname].attrib['name'] = newfieldname
                    fields[newfieldname].attrib['fieldname'] = self.upper_camel_case(newfieldname, stripPrefix=True, stripSuffix=True)
                    fields[newfieldname].attrib['descr'] = ""
                    fields[newfieldname].attrib['dropped'] = "False"

                # mark the old field
                fields[fieldname].attrib['dropped'] = "True"

            # replace fields in uniquekey
            for uniquekey in uniquekeys:
                uniquekey.attrib['thisFields'] = uniquekey.attrib['thisFields'].replace(' ', '').replace(key.attrib['thisFields'].replace(' ', ''), newfieldname)
            primarykey.attrib['thisFields'] = primarykey.attrib['thisFields'].replace(' ', '').replace(key.attrib['thisFields'].replace(' ', ''), newfieldname)
            # add new foreignkey
            key.attrib['thisFields'] = newfieldname
            foreignkeys.append(key)

        # first process fields of primary key
        for fieldname in primarykey.attrib['thisFields'].replace(' ', '').split(','):
            self.process_field(f, tableNode.attrib['name'], className, fields[fieldname], primarykey, foreignkeys)

        # then process the other fields
        for fieldname in fields.keys():
            if fieldname in primarykey.attrib['thisFields']:
                continue
            if fields[fieldname].attrib['dropped'] == "False":
                self.process_field(f, tableNode.attrib['name'], className, fields[fieldname], primarykey, foreignkeys)

        if len(uniquekeys) > 0:
            f.write(f'\n  class Meta:')
            f.write(f'\n    constraints = [')
            for key in uniquekeys:
                uniquefields = []
                for field in key.attrib['thisFields'].replace(' ', '').split(','):
                    if fields[field].attrib['dropped'] == "True":
                        # ignore dropped field of composite key
                        continue
                    uniquefields.append("'" + fields[field].attrib['fieldname'] + "'")
                f.write(f"\n      models.UniqueConstraint(name='{key.attrib['name']}', fields=[{self.concat(uniquefields)}]),")
            f.write(f'\n    ]')

    def get_tables_without_unsatisfied_dependancies(self, tables):
        for key in tables.keys():
            unsatisfied_dep = False
            for child in tables[key]:
                if child.tag == 'foreignkey':
                    if child.attrib['otherTable'] != key:
                        if child.attrib['otherTable'] in tables.keys():
                            unsatisfied_dep = True
            if not unsatisfied_dep:
                return tables[key]

    def process_database(self, f, root):

        tables = {}

        for child in root:
            # print(f"{child.tag} {child.attrib['name']}")

            if child.tag == "table":
                tables[child.attrib['name']] = child

        # do a topological sort, by dependancies
        sorted_tables = []

        # start with s_user
        sorted_tables.append(tables['s_user'])
        del tables['s_user']
        while len(tables) > 0:
            table = self.get_tables_without_unsatisfied_dependancies(tables)
            if table is None:
                raise Exception(f"problem with Topological sort")
            sorted_tables.append(table)
            del tables[table.attrib['name']]

        for table in sorted_tables:
            self.process_table(f, table)

    def handle(self, *args, **options):
        tree = etree.parse("definitions/petra.xml")

        with open('apps/data/models.py', 'w') as f:
            f.write('# this is a generated file.\n')
            f.write('# do not edit manually, but run: python manage.py createmodel\n')
            f.write('from django.db import models\n')
            self.process_database(f, tree.getroot())
