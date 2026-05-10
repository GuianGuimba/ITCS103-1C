import openpyxl as op

workbook = op.load_workbook("excel.xlsx")
sheet = workbook.active

value = sheet['A1'].value
print(value)

#Reading a specific cell inside a Workbook/Excel File