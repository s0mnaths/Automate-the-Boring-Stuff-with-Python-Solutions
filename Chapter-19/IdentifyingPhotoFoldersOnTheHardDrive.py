import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('/home'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        if not (filename.lower().endswith('.jpg') or filename.lower().endswith('.png')):
            numNonPhotoFiles += 1
            continue    
        try:
            im = Image.open(os.path.join(foldername, filename))
            width, height = im.size
        except OSError:
            continue
        
        if width > 500 and height > 500:
            numPhotoFiles += 1
        else:
            numNonPhotoFiles += 1

    if numPhotoFiles>numNonPhotoFiles:
        print(os.path.abspath(foldername))