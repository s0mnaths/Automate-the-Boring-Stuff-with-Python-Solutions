import re

oldFile = open('oldMadlibs.txt')
text = oldFile.read()
oldFile.close()

regex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
while regex.search(text) !=None:
    word = input(f'Enter a {regex.search(text).group().lower()}: ')
    text = regex.sub(word, text, 1)
print(text)
newFile = open('newMadlibs.txt', 'w')
newFile.write(text)
newFile.close()