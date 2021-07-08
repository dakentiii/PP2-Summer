import os
import os.path
import time 
import shutil
from pathlib import Path

path = os.getcwd()
os.remove("test.txt")

os.rename(r'file path\OLD test.txt.file type',r'file path\NEW test_1.txt.file type')

with open("test.txt", "a") as myfile:
    myfile.write("appended text")
    f=open("Diabetes.txt",'r')
f.read()

path = Path("/text.txt")
print(path.parent.absolute())

os.rename(src, dst)

totalFiles = 0
totalDir = 0
for base, dirs, files in os.walk(APP_FOLDER):
    print('Searching in : ',base)
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1
        print('Total number of files',totalFiles)
print('Total Number of directories',totalDir)
print('Total:',(totalDir + totalFiles))

arr = os.listdir('.')
print(arr)