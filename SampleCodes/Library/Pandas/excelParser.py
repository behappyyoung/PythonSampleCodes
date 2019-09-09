###
#
# Excel file parser with Pandas Library
#
###

import pandas
import sys
import os
import math


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ExcelParser(object):
    return_array = []

    def __init__(self):
        self.return_array = []

    def parse_as_array(self, fileName):
        try:
            os.path.isfile(fileName)
            os.path.exists(fileName)

            xls = pandas.ExcelFile(fileName)
            # print(xls, xls.sheet_names)
            self.return_array.append(xls.sheet_names)
            inter_array = []
            for shName in xls.sheet_names:
                df = xls.parse(shName)
                print('%s Sheet Name : %s %s' % (bcolors.WARNING, shName, bcolors.ENDC))

                # print(df.__dict__)

                # print list of column names
                # self.return_array.append('columns', list(df))
                # self.return_array.append('culumns', df.columns)

                for index, row in df.iterrows():
                    inter_array.append({index: row})

                # for d in df.iloc[:, 5]:
                #     if isinstance(d, str) or not math.isnan(d):
                #         # print(d)
                #         self.return_array.append(d)
                self.return_array.append({shName: inter_array})

            # sheet1 = xls.parse(0)
            # sheet2 = xls.parse(1)
            # print(sheet1)
            # print(sheet2)

        except Exception as e:
            e_message = e.message if hasattr(e, 'message') else ','.join(map(str, e.args))
            self.return_array.append(e_message)

        return self.return_array

    @classmethod
    def main(cls, file_name):

        try:
            ep = ExcelParser()
            return_array = ep.parse_as_array(file_name)
            print(return_array)
        except Exception as e:
            e_message = e.message if hasattr(e, 'message') else ','.join(map(str, e.args))
            print(e_message)
            exit(1)


if __name__ == '__main__':
    file_name = str(sys.argv[1]) if len(sys.argv) > 1 else 'test.xlsx'
    ExcelParser.main(file_name)