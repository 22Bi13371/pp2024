from domains import *


def main():
    school = School()
    while True:
        print_menu = "-----------MENU----------- \n0)Exit program \n1)Input student(s) info \n2)Input course(s) info \n3)Input student marks \n4)List courses \n5)List students \n6)List student marks \n7)List student GPAs"
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
                school.input_student_info()
            case 2:
                school.input_course_info()
            case 3:
                school.input_student_marks()
            case 4:
                school.list_courses()
            case 5:
                school.list_students()
            case 6:
                school.show_student_marks()
            case 7:
                school.show_student_gpas()
            case _:
                print("Invalid option!")
                continue


if __name__ == "__main__":
    main()
