from sys import argv
from zipfile import ZipFile


script, curFile = argv


print("Here's your file %r:" % curFile)

# zf = ZipFile(filename)
# zf.extractall(path='Files', members=None, pwd=None)
try:
    with ZipFile(curFile, 'r') as zipObj:
       # Get a list of all archived file names from the zip
       listOfFileNames = zipObj.namelist()
       # Iterate over the file names
       for fileName in listOfFileNames:
           print(fileName)
           if fileName.endswith('.png'):
               # Extract a single file from zip
               zipObj.extract(fileName, 'Files')
except Exception as e:
    print(e)