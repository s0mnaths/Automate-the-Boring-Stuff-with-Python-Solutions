import re,sys

inputDate=input('Enter Date in DD/MM/YYYY: ')
date=re.compile(r'([0-3]\d)/([01]\d)/([1-2]\d{3})')
RegexDate=date.findall(inputDate)

if RegexDate==None:
    print('WRONG: Date not in format DD/MM/YYYY .')
    sys.exit()
else:
    for day,month,year in RegexDate:
        day=int(day)
        month=int(month)
        year=int(year)

        if (month==4 or month==6 or month==9 or month==11):
            if day==31:
                print('WRONG: Invalid Date')
        elif month==2:
            if year%4==0:
                if not day in range(1,30):
                    print('WRONG: Invalid Date')
            else:
                if not day in range(1,29):
                    print('WRONG: Invalid Date')
        print('CORRECT: Valid date in correct DD/MM/YYYY formmat')