from lxml import etree

def upper_camel_case(s):
    return s.replace('_', ' ').title().replace(" ", "")

def process_field(f, fieldNode):
    fieldName = upper_camel_case(fieldNode.attrib['name'])[1:-1]
    fieldType = fieldNode.attrib['type']

    if 'descr' in fieldNode.attrib and fieldNode.attrib['descr'].strip(' '):
        f.write(f"  # {fieldNode.attrib['descr']}\n")

    default = ''
    null = ''
    if 'notnull' in fieldNode.attrib:
        if fieldNode.attrib['notnull'] == 'yes':
            null = ', null=False, blank=False'

    if fieldType == "varchar" or fieldType == "text":
        maxlength = 20
        if 'format' in fieldNode.attrib:
            maxlength = fieldNode.attrib['format'][2:-1]
        if 'initial' in fieldNode.attrib:
            default = f", default='{fieldNode.attrib['initial']}'"

        f.write(f"  {fieldName} = models.CharField(max_length={maxlength}{default}{null})\n")
    elif fieldType == "bit":
        if 'initial' in fieldNode.attrib:
            if fieldNode.attrib['initial'].lower() == 'yes':
                default = f"default=True"
            elif fieldNode.attrib['initial'].lower() == 'no':
                default = f"default=False"

        f.write(f"  {fieldName} = models.BooleanField({default}{null})\n")
    elif fieldType == "integer" or (fieldType == "number" and not 'decimals' in fieldNode.attrib):
        if 'initial' in fieldNode.attrib and fieldNode.attrib['initial'] != '?':
            default = f"default={fieldNode.attrib['initial']}"
        if not default and null:
            null = null[2:]
        f.write(f"  {fieldName} = models.IntegerField({default}{null})\n")
    elif fieldType == "number" and 'decimals' in fieldNode.attrib:
        if 'initial' in fieldNode.attrib:
            default = f", default={fieldNode.attrib['initial']}"
        f.write(f"  {fieldName} = models.DecimalField(max_digits={fieldNode.attrib['length']}, decimal_places={fieldNode.attrib['decimals']}{default}{null})\n")
    elif fieldType == "date" or fieldType == "datetime":
        null = null.strip(',')
        f.write(f"  {fieldName} = models.DateTimeField({null})\n")


def process_table(f, tableNode):
    className = upper_camel_case(tableNode.attrib['name'])
    f.write(f'\n\nclass {className}(models.Model):\n')

    for child in tableNode:
        if child.tag == "tablefield":
            process_field(f, child)

def process_database(f, root):
    for child in root:
        print(f"{child.tag} {child.attrib['name']}")

        if child.tag == "table":
            process_table(f, child)

tree = etree.parse("../definitions/petra.xml")

with open('../apps/data/models.py', 'w') as f:
    f.write('from django.db import models\n')
    process_database(f, tree.getroot())
