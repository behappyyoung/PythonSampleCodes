from PIL import ImageGrab
# import win32com.client as win32
import pandas


# excel = win32.gencache.EnsureDispatch('Excel.Application')
# workbook = excel.Workbooks.Open(r'files\test.xlsx')

workbook = pandas.ExcelFile('test.xlsx')


for sheet in workbook.Worksheets:
    for i, shape in enumerate(sheet.Shapes):
        if shape.Name.startswith('Picture'):
            shape.Copy()
            image = ImageGrab.grabclipboard()
            image.save('{}.jpg'.format(i+1), 'jpeg')
