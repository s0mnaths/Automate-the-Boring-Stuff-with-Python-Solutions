#USAGE: in the commmand line run: python3 ch-14b.py <spreadsheet Name>
                                                    #second argument should be the spreadsheet name along with extension
                                                    #keep the spreadsheet in the same directory as this .py script

import ezsheets,sys

spreadsheetOld=sys.argv[1]
ss=ezsheets.upload(spreadsheetOld)
print('Spreadsheet name: '+ ss.title)
ss.downloadAsCSV()
print('Done!')