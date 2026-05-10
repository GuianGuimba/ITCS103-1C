import openpyxl as op

wbk = op.load_workbook("excel.xlsx")
sheet = wbk.active

for rows in sheet.iter_rows(values_only=True):
    print(rows)

#Reading all rows in Workbook/Excel file