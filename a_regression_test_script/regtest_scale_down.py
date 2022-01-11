# https://www.oreilly.com/library/view/programming-python-second/0596000855/ch04s04.html

import os, sys                            # get unix, python services 
from stat import ST_SIZE                  # or use os.path.getsize
from glob import glob                     # file name expansion
from os.path import exists                # file exists test
from time import time, ctime              # time functions

print( 'RegTest start.') 
print( 'user:', os.environ['USER'])         # environment variables
print( 'path:', os.getcwd())              # current directory
print( 'time:', ctime(time()), '\n')
program = sys.argv[1]                     # two command-line args
testdir = sys.argv[2]

for test in glob(testdir + '/*.in'):      # for all matching input files
    print( f"test file: {test}")

print( 'RegTest done:', ctime(time()))
