import pandas, sys, os, math


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


fileName = str(sys.argv[1]) if len(sys.argv) > 1 else 'test.xlsx'

try:
    os.path.isfile(fileName)
    os.path.exists(fileName)

    xls = pandas.ExcelFile(fileName)
    print(xls, xls.sheet_names)

    for shName in xls.sheet_names:
        df = xls.parse(shName)
        print('%s Sheet Name : %s %s' % (bcolors.WARNING, shName, bcolors.ENDC))

        # print(df.__dict__)

        # print list of column names
        print('columns', list(df))
        print('culumns', df.columns)

        for index, row in df.iterrows():
            print(index, row)

        for d in df.iloc[:, 5]:
            if isinstance(d, str) or not math.isnan(d):
                print(d)

    # sheet1 = xls.parse(0)
    # sheet2 = xls.parse(1)
    # print(sheet1)
    # print(sheet2)
except Exception as e:
    raise e