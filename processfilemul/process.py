from sys import argv

import os
#import os, winshell
#from win32client.client import Dispatch

script = argv
name = str(script[0])

cmd = 'start payload.txt'
os.system(cmd)
for i in range(1,5):
  os.system(cmd)