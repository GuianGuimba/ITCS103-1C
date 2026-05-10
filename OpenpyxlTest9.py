import openpyxl as op

wbk = op.load_workbook("excel.xlsx")
sheet = wbk.active

for cols in sheet.iter_cols(values_only=True):
    print(cols)

#Reading all columns in Workbook/Excel File