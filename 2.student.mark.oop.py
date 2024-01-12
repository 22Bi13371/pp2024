class Student:
   def __init__(self, id, name, dob):
       self.id = id
       self.name = name
       self.dob = dob
       self.marks = {}

   def add_mark(self, course_id, mark):
       self.marks[course_id] = mark

class Course:
   def __init__(self, id, name):
       self.id = id
       self.name = name

class School:
   def __init__(self):
       self.students = []
       self.courses = []

   def add_student(self, student):
       self.students.append(student)

   def add_course(self, course):
       self.courses.append(course)

   def input_student_info(self):
       num_students = int(input("Enter the number of students: "))
       for _ in range(num_students):
           id = input("Enter student ID: ")
           name = input("Enter student name: ")
           dob = input("Enter student DoB: ")
           self.add_student(Student(id, name, dob))

   def input_course_info(self):
       num_courses = int(input("Enter the number of courses: "))
       for _ in range(num_courses):
           id = input("Enter course ID: ")
           name = input("Enter course name: ")
           self.add_course(Course(id, name))

   def input_student_marks(self):
       if not self.courses:
           print("There are no courses in the database!")
           return
       selected_course = input("Select a course ID: ")
       for student in self.students:
           marks = float(input(f"Enter marks for student {student.id} in course {selected_course}: "))
           student.add_mark(selected_course, marks)

   def list_courses(self):
       print("Courses:")
       for course in self.courses:
           print(f"ID: {course.id}, Name: {course.name}")

   def list_students(self):
       print("Students:")
       for student in self.students:
           print(f"ID: {student.id}, Name: {student.name}, DoB: {student.dob}")

   def show_student_marks(self):
       if not self.courses or not self.students:
           return
       selected_course = input("Select a course ID: ")
       print(f"Marks for course {selected_course}:")
       for student in self.students:
           print(f"Student {student.id}: {student.marks.get(selected_course, 'Not enrolled')}")

   def run(self):
       while True:
        print_menu = "-----------MENU----------- \n0)Exit program \n1)Input student(s) info \n2)Input course(s) info \n3)Input student marks \n4)List courses \n5)List students \n6)List student marks"
        print(print_menu)
        try:
            menu_selector = int(input("You chose? ")) 
            pass
        except ValueError:
            print("Integer or else....\n")
            continue

        match menu_selector:
            case 0:
                print("Exitting program...")
                break
            case 1:
                self.input_student_info()
            case 2:
                self.input_course_info()
            case 3:
                self.input_student_marks()
            case 4:
                self.list_courses()
            case 5:
                self.list_students()
            case 6:
                self.show_student_marks()
            case _:
                print("Invalid option!")
                continue

if __name__ == "__main__":
   school = School()
   school.run()
