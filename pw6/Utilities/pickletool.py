from pathlib import Path
import pickle
from domains import *

files = ["courses.txt", "marks.txt", "students.txt"]

def storeData(school):
    with open(".data/Database.json", "a+b") as file:
        pickle.dump(school, file)

def loadData(school):
    try:
        with open(".data/Database.json", "rb") as file:
            school = pickle.load(file)
    except FileNotFoundError:
        print("No Database.json can be found!")