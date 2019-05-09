
from sys import argv
from zipfile import ZipFile

script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)

ZipFile.extractall(path=None, members=None, pwd=None)