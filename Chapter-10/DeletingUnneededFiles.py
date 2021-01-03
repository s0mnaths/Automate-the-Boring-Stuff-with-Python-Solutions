import os
from pathlib import Path

for folder, subFolders, files in os.walk(Path.cwd()):
    for file in files:
        filePath=os.path.join(folder,file)
        if os.path.getsize(filePath)>500:
            print('File Name: '+file+"      File Path: "+filePath)