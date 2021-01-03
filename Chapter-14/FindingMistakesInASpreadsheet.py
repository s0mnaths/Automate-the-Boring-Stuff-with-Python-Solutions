import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
i=2
while(ss[0].getRow(i)[0]!=''):
    if int(ss[0].getRow(i)[0]) * int(ss[0].getRow(i)[1]) != int(ss[0].getRow(i)[2]):
        print('Incorrect total at row: ', i)
    i+=1
print('Done!')