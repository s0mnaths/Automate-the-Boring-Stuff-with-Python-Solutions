import os, shutil
from pathlib import Path

p=Path.cwd()
extension=input('Enter extension: ')
newFolderName=input('Enter new Folder name: ')
os.makedirs(p/newFolderName)
#extension='*.'+extension

for folderNames, subFolderNames, fileNames in os.walk(p):
    for fileName in fileNames:
        if fileName.endswith(extension):
            shutil.copy(os.path.join(folderNames, fileName), p/newFolderName/fileName)