#USAGE: in the commmand line run: python3 ch-14a.py <spreadsheetID>
                                                    #second argument should be the spreadsheetId

import ezsheets,sys

spreadsheetID=sys.argv[1]
ss=ezsheets.Spreadsheet(spreadsheetID)
print('Spreadsheet name: '+ ss.title)
sheet=ss[0]
print('sheet titile: '+ sheet.title)
print(sheet.rowCount)
emailColumn=sheet.getColumn(3)
i=1
emailList=[]
while(emailColumn[i]!=''):
    emailList.append(emailColumn[i])
    print(emailColumn[i])
    i+=1
print("All emails stored list- 'emailList'")
print('Done!')