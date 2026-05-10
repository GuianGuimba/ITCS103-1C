import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active
workbook.save("excel.xlsx")

#Generating a Workbook / Excel file