import tarfile as tar
import gzip
from pathlib import Path

files = ["courses.txt", "marks.txt", "students.txt"]


def validate_files(filelist):
    files_present = []
    for file in filelist:
        if Path(f"./data/{file}").exists():
            files_present.append(file)
    return files_present


def remove_data():
    files_present = validate_files(files)
    print(files_present)
    if len(files_present) == 3:
        for file in files_present:
            file_to_remove = Path(f"./data/{file}")
            file_to_remove.unlink()
    else:
        print(f"There are not enough files(3) to remove!")


def compress():
    files_present = validate_files(files)
    if len(files_present) == 3:
        with tar.open("./data/students.dat", "w:gz") as studentFile:
            for file in files_present:
                studentFile.add(f"./data/{file}", arcname=file)
    else:
        print("You must input all data before compressing!")

def decompress():
    files_present = validate_files(files)
    if len(files_present) == 3:
        return
    elif Path(f"./data/students.dat").exists():
        with tar.open("./data/students.dat", "r:gz") as studentFile:
            studentFile.extractall("./data")
    else:
        print("No students.dat!")