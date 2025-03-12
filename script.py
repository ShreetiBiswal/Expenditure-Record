import os
from pathlib import Path
from datetime import datetime
import csv

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


def addEntry(amount, category,year,file,comments=""):
    folder_path = Path(f"./Data/{year}")
    file_path = folder_path / f"{file}.csv"  

    folder_path.mkdir(parents=True, exist_ok=True)

    file_exists = file_path.exists()

    new_data = {"amount": amount, "category": category, "comments": comments}

    with open(file_path, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["amount", "category", "comments"])

        if not file_exists:
            writer.writeheader()
        
        writer.writerow(new_data)

    print(f"Entry added to {file_path} for today's expenditure!!!")

def addEntryToday(amount, category,comments=""):
    addEntry(amount,category,getYear(),getMonthDay(),comments)

# with open("./Data/2025/March[12].csv",'r') as f:
#     reader=csv.DictReader(f)
#     for row in reader:
#         print(row)

addEntryToday(150,"food","biriyani")