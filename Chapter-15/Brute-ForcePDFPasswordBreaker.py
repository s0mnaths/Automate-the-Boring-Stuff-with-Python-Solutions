import PyPDF2

found=False
pdfReader=PyPDF2.PdfFileReader(open('somePdfFile.pdf', 'rb'))
file=open('dictionary.txt')
listOfWords=file.readlines()
for word in listOfWords:
    if pdfReader.decrypt(word.strip())==1:
        print('-->Password found: ',word.strip())
        found=True
        break
    elif pdfReader.decrypt(word.strip().lower())==1:
        print('-->Password found: ',word.strip().lower())
        found=True
        break

if found==False:
    print('-->Password not found')


print('Done!')