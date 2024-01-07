def input_num_students():
   return int(input("Enter the number of students: "))

def input_student_info(num_students):
   students = {}
   for _ in range(num_students):
       id = input("Enter student ID: ")
       name = input("Enter student name: ")
       dob = input("Enter student DoB: ")
       students[id] = {"name": name, "dob": dob, "marks": {}}
   return students

def input_num_courses():
   return int(input("Enter the number of courses: "))

def input_course_info(num_courses):
   courses = {}
   for _ in range(num_courses):
       id = input("Enter course ID: ")
       name = input("Enter course name: ")
       courses[id] = name
   return courses

def select_course(courses):
   return input("Select a course ID: ")

def input_student_marks(students, selected_course):
   for student_id, student_info in students.items():
       marks = float(input(f"Enter marks for student {student_id} in course {selected_course}: "))
       student_info["marks"][selected_course] = marks

def list_courses(courses):
   print("Courses:")
   for course_id, course_name in courses.items():
       print(f"ID: {course_id}, Name: {course_name}")

def list_students(students):
   print("Students:")
   for student_id, student_info in students.items():
       print(f"ID: {student_id}, Name: {student_info['name']}, DoB: {student_info['dob']}")

def show_student_marks(students, selected_course):
   print(f"Marks for course {selected_course}:")
   for student_id, student_info in students.items():
       print(f"Student {student_id}: {student_info['marks'].get(selected_course, 'Not enrolled')}") 

def main():
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
            num_students = input_num_students()
            students = input_student_info(num_students)
         case 2:
            num_courses = input_num_courses()
            courses = input_course_info(num_courses)
         case 3:
            if 'courses' not in locals():
               print("There are no courses in the database!")
               continue
            elif 'students' not in locals():
               print("There are no students in the database!")
               continue
            else:
               selected_course = select_course(courses)
               input_student_marks(students, selected_course)
         case 4:
            if 'courses' not in locals():
               print("There are no courses in the database!")
               continue
            else:
               list_courses(courses)
         case 5:
            if 'students' not in locals():
               print("There are no courses in the database!")
               continue
            else:
               list_students(students)
         case 6:
            show_student_marks(students, selected_course)
            if 'selected_course' not in locals():
               print("Student(s) marks are not yet inputted!")
               continue
            if 'students' not in locals():
               print("There are no students in the database!")
               continue
            else:
               show_student_marks(students, selected_course)
         case _:
            print("Invalid option!")
            continue

if __name__ == "__main__":
   main()