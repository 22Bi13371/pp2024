import tarfile as tar
import gzip
from pathlib import Path
from domains import Course, Student

files = ["courses.txt", "marks.txt", "students.txt"]


def validate_files(filelist):
    files_present = []
    for file in filelist:
        if Path(f"./data/{file}").exists():
            files_present.append(file)
    return files_present

def loadData(school):
    files_present = validate_files(files)
    if len(files_present) == 3:
        print(f"Found all 3 files \nNow loading data...")
        with open("./data/students.txt", 'r') as studentFile:
            for line in studentFile:
                id, name, dob = line.strip(), studentFile.readline().strip(), studentFile.readline().strip()
                school.add_student(Student.Student(id, name, dob))
        with open("./data/courses.txt", 'r') as courseFile:
            for line in courseFile:
                id, name, = line.strip(), courseFile.readline().strip(),
                school.add_course(Course.Course(id, name))
        with open("./data/marks.txt", 'r') as marksFile:
            for line in marksFile:
                student_id, mark, course_id = line.strip(), marksFile.readline().strip(), marksFile.readline().strip()
                for student in school.getstudents():
                    try:
                        student.add_mark(course_id, mark)
                        pass
                    except IOError:
                        print("error!")
                        continue
    else:
        print("There are not enough required files to load!")

def remove_data():
    files_present = validate_files(files)
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