import pandas, sys, os

fileName = str(sys.argv[1]) if len(sys.argv) > 1 else 'test.xlsx'

try:
    os.path.isfile(fileName)
    os.path.exists(fileName)

    xls = pandas.ExcelFile(fileName)
    print(xls, xls.sheet_names)
    df = xls.parse('Sheet1')
    print(df)
    sheet1 = xls.parse(0)
    sheet2 = xls.parse(1)
    print(sheet1)
    print(sheet2)
except Exception as e:
    raise e