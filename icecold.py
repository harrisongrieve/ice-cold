#!python

from openpyxl import load_workbook

wb = load_workbook('sample_leads.xlsx')

ws = wb.get_active_sheet()

for i in ws.range('A2:A5'):
    print i[0].value
