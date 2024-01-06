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

# def menu_selector(menu_selector):
#    if menu_selector == 0:
#       print("Exitting program")
#       return 0
       
def menu_selector(menu_selector):
   match menu_selector:
      case 0:
         print("Exitting program...")
      case 1:
         return input_num_students
      case 2:
         return input_student_info
      

      case _:
         print("Invalid option!")
      

def main():
   num_students = input_num_students()
   students = input_student_info(num_students)
   num_courses = input_num_courses()
   courses = input_course_info(num_courses)
   selected_course = select_course(courses)
   input_student_marks(students, selected_course)
   list_courses(courses)
   list_students(students)
   show_student_marks(students, selected_course)

   

if __name__ == "__main__":
   main()