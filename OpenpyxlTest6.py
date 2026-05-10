import openpyxl as op

workbook = op.Workbook()

sheet = workbook.active

sheet['A1'] = "PRODUCT"
sheet['B1'] = "PRICE"
sheet['C1'] = "QUANTITY"
sheet['D1'] = "TOTAL AMMOUNT"
sheet['A2'] = "Pencil"
sheet['B2'] = "14"
sheet['C2'] = "4"

workbook.save("excel.xlsx")

#Writing Inside Workbook/Excel file