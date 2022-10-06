#!/usr/bin/env python3.8

#knutnation
"""
pdf password remover
Remove the password for ALL files in given path
- need "pdftk" installed (just tested with Ubuntu 22.04 -> "sudo apt install pdftk")
- non recursive (ignores directory's in path)
- creates a Folder in given path (without/)
- threading for a but parallel workload to be a bit faster ^^
- uses threading, time, subprocess, os and sys (i know... a lot of stuff, improve it =P)
- pipes all warnings to >/dev/null 2>&1
"""

import threading as th
import time
import subprocess
import os

import sys

GGlen = 4201337

class major():
    def __init__(self, path, pw):
        self.path = path
        self.pw = pw
        mkdir = "mkdir " + self.path + "without/" + " >/dev/null 2>&1"
        try:
            mkdir = subprocess.check_output(mkdir, shell=True)
        except:
            pass
        print("\n[\"" + self.path + "\"] get password removed")

    def makeAlist(self):
        global GGlen
        self.filelist = os.listdir(self.path)
        GGlen = len(self.filelist)

    def tk(self):
        global GGlen
        self.tker = []
        for file in self.filelist:
            if(os.path.isdir(self.path + file)):
                GGlen = GGlen - 1
                continue
            tkk = tk(file, self.path, self.pw)
            self.tker.append(tkk)
            self.tker[-1].start()

class tk( th.Thread ):
    def __init__(self, file, path, pw):
        th.Thread.__init__(self)
        self.file = file
        self.oldpath = path + file
        self.newpath = path + "ohne/" + file
        self.pw = pw

    def run(self):
        global GGlen
        befehl = "pdftk " + self.oldpath + " input_pw " + self.pw + " output " + self.newpath + " >/dev/null 2>&1"
        #print(befehl)
        self.tkk = subprocess.check_output(befehl, shell=True)
        GGlen = GGlen - 1
            #pdftk crypt01__lec.pdf input_pw Euklid18 output test.pdf

if __name__ == "__main__":
    if(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print("./tkskript.py path password")
        print("or")
        print("python3 tkskript.py path password")
    else:
        macher = major(sys.argv[1], sys.argv[2])
        macher.makeAlist()
        macher.tk()
        while (GGlen > 0):#wait for all hreads to finish
            time.sleep(0.2)
        print("Finished.")
