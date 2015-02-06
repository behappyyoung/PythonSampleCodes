import os
dirname = os.path.dirname(os.path.realpath(__file__))

####### using listdir
dirlist = os.listdir(dirname)

######## using glob
import glob
globlist = glob.glob(dirname+'/*')

####### using subprocess
from subprocess import Popen, PIPE
def listdir_shell(path, *lsargs):
    p = Popen(('ls', path) + lsargs, shell=False, stdout=PIPE, close_fds=True)
    return [path.rstrip('\n') for path in p.stdout.readlines()]

sublist = listdir_shell(dirname, '-t')[:10]

print('\n dirname : ' + dirname + ' \n lists \n')
print('\n using dirlist ')
print( dirlist)
print('\n using glob : ')

from pprint import pprint
pprint( globlist)
print('\n using subprocess : ')
pprint(sublist)

