import os
dirname = os.path.dirname(os.path.realpath(__file__))
dirlist = os.listdir(dirname)

import glob
globlist = glob.glob(dirname+'/*')



print('dirname : ' + dirname)
print('\n current dir list ')
print( dirlist)
print('\n using glob : ')

from pprint import pprint
pprint( globlist)


