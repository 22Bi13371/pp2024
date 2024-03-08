from pathlib import Path
import pickle
from domains import School, Student, Course
from threading import Thread
import time

files = []
filename = "./data/Student.json"


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def storeData(school):
    try:
        with open(filename,'wb') as file:
            time.sleep(1)
            print("Saving is sleeping for 1s...")
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