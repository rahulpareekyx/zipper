__author__ = 'RAHUL PAREEK'
import os

path = raw_input("Enter zip file path > ")
file = raw_input("Enter zip file name > ")
unzip_program="C:\Users\Rahul\Desktop\Python\unzip.exe"
os.chdir(path)
os.system(unzip_program +" " +"\""+ files +"\"" )
