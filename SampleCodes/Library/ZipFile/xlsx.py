import zipfile
zip = zipfile.ZipFile('files/test.xlsx')
print(zip.namelist())
zip.extract('xl/media/image1.png', 'files/media.png')
