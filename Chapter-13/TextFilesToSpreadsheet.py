import openpyxl
from pathlib import Path

p= Path().cwd()
listOfTextFiles=list(p.glob('*.txt'))

wb=openpyxl.Workbook()
sheet=wb.active

for i in range(len(listOfTextFiles)):
    file=open(listOfTextFiles[i])
    fileContent=file.readlines()
    for j in range(len(fileContent)):
        sheet.cell(row=j+1,column=i+1).value=str(fileContent[j])
    file.close()
wb.save('textToWorksheet.xlsx')
wb.close()