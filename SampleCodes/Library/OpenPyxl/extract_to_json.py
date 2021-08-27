from openpyxl import load_workbook
import json

workbook = load_workbook(filename="KAPA_sequences.xlsx")
workbook_sheet = workbook.worksheets[0]
output_json = {}
for x in range(5, 101):
    print(workbook_sheet[f'B{x}'].value, workbook_sheet[f'C{x}'].value, workbook_sheet[f'E{x}'].value)
    output_json[workbook_sheet[f'B{x}'].value.replace(' ', '_')] = {'p7_seq': workbook_sheet[f'C{x}'].value, 'p5_seq': workbook_sheet[f'E{x}'].value}

print(output_json)
output_file = 'kapa_sequence.json'
with open(output_file, 'w+') as f:
    f.write(json.dumps(output_json))

