from pathlib import Path
import pickle
from domains import *

files = []
filename = "./data/Student.json"


def storeData(school):
    try:
        with open(filename,'wb') as file:
            pickle.dump(school, file)
    except IOError:
        print("Error! File not found")


def loadData():
    try:
        if Path(filename).exists():
            with open(filename, "rb") as file:
                return pickle.load(file)
        else:
            return School.School()
    except FileNotFoundError:
        print("No Database.json can be found!")