from pathlib import Path
import re

regex=input('Enter a regex: ')
p= Path().cwd()

list1=list(p.glob('*.txt'))
for i in range(len(list1)):
    fileContent=list1[i].read_text()
    searchRegex=re.compile(regex)
    result=searchRegex.findall(fileContent)
    print(result)