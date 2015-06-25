__author__ = 'RAHUL PAREEK'
from sys import argv
import os

script,logsdir = argv
zip_program="C:\Users\Rahul\Desktop\Python\zip.exe"
zipfile = raw_input("Enter name of zip file: ")
for files in os.listdir(logsdir):
    if files.endswith(".srt"):
        os.chdir(logsdir)
        os.system(zip_program + " " +  zipfile +" "+"\""+ files +"\"")
        os.remove(files)
