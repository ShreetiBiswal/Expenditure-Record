import os
from pathlib import Path
from datetime import datetime

def getFiles(pathString):
    path=Path(pathString)
    files=[f for f in path.iterdir() if f.is_file()]
    return files

def getFolders(pathString):
    path=Path(pathString)
    folders=[f.name for f in path.iterdir() if f.is_dir()]
    return folders

def getYear():
    return datetime.today().strftime("%Y")

def getMonthDay():
    return datetime.today().strftime("%B[%d]")

print(getMonthDay())