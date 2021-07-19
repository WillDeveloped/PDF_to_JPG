#This program walks a directory, and converts those pdf files
#into jpeg files

from pdf2image import convert_from_path
import os
import os.path

DIR_TO_WALK = ""    #Insert directory to walk here. For instance, if I wanted to walk all files in directory "Documents",
                    #I would set this to: "C:\Users\william\Documents"
 
for root, dirs, files in os.walk(DIR_TO_WALK):
    for name in files:
        images = convert_from_path(DIR_TO_WALK + "/" + name)
        fileName = name.split(".")[0] + '.jpg'
        print(fileName)
        for i in range(len(images)):
            images[i].save(fileName, 'JPEG')
