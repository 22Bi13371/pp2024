import tarfile as tar
import gzip
from pathlib2 import Path


def validate_files(filelist):
    files_present = []
    for file in filelist:
        if Path(f"./data/{file}").exists():
            files_present.append(file)
    return files_present


def compress():
    files = ["courses.txt", "marks.txt", "students.txt"]
    files_present = validate_files(files)
    if len(files_present) == 3:
        with tar.open("./data/students.dat", "w:gz") as studentFile:
            for file in files_present:
                studentFile.add(f"./data/{file}", arcname=file)

def decompress():
    with tar.open("./data/students.dat", "r:gz") as studentFile:
        studentFile.extractall("./data")