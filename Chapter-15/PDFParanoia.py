#USAGE : 
#To Encrypt: In terminal run--> python3 ch-15a.py encrypt <password>
#To Decrypt: In terminal run--> python3 ch-15a.py decrypt <password>

import os, sys, PyPDF2

def encrypt():
    for folder, subFolder, files in os.walk('.'):
        for fileName in files:
            if fileName.endswith('.pdf'):
                oldPath=os.path.join(folder, fileName)
                pdfReader=PyPDF2.PdfFileReader(open(oldPath, 'rb'))
                if pdfReader.isEncrypted==False:    
                    pdfWriter=PyPDF2.PdfFileWriter()
                    for page in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(page))
                    pdfWriter.encrypt(password)
                    newPath=oldPath[:-4]+'_encrypted.pdf'
                    newFile=open(newPath,'wb')
                    pdfWriter.write(newFile)
                    newFile.close()

                    pdfReader=PyPDF2.PdfFileReader(newPath,'rb')
                    if pdfReader.isEncrypted==True and pdfReader.decrypt(password)==1:
                        os.remove(oldPath)

def decrypt():
    for folder, subFolder, files in os.walk('.'):
        for fileName in files:
            if fileName.endswith('.pdf'):
                oldPath=os.path.join(folder, fileName)
                pdfReader=PyPDF2.PdfFileReader(open(oldPath, 'rb'))
                if pdfReader.isEncrypted==True:
                    if pdfReader.decrypt(password)==1:
                        pdfReader.decrypt(password)
                        pdfWriter=PyPDF2.PdfFileWriter()
                        for page in range(pdfReader.numPages):
                            pdfWriter.addPage(pdfReader.getPage(page))
                        newPath=oldPath[:-4]+'_decrypted.pdf'
                        newFile=open(newPath,'wb')
                        pdfWriter.write(newFile)
                        newFile.close()
                    else:
                        print('Error! Wrong password for file at path', oldPath)
password=sys.argv[2]
if sys.argv[1]=='encrypt':
    encrypt()
elif sys.argv[1]=='decrypt':
    decrypt()
else:
    print('Wrong 2nd argument \r Should either be "encrypt" or "decrypt"')
#print(sys.argv[1])
print('Program end') 