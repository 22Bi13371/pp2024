from domains import *
import output
import inputs
import threading
from Utilities import *


def main():
    school = School.School()
    compression.decompress()
    # compression.loadData(school)
    # school = pickletool.loadData()

    load_thread = pickletool.ThreadWithReturnValue(target=pickletool.loadData)
    load_thread.start()
    school = load_thread.join()
    save_thread = threading.Thread(target=pickletool.storeData, args=(school,))
    save_thread.start()

    while True:
        print_menu = "-----------MENU----------- \n0)Exit program \n1)Input student(s) info \n2)Input course(s) info \n3)Input student marks \n4)List courses \n5)List students \n6)List student marks \n7)List student GPAs \n8)Remove student files"
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
                # pickletool.storeData(school)
                save_thread.join()
                compression.compress()
                break
            case 1:
                inputs.input_student_info(school)
            case 2:
                inputs.input_course_info(school)
            case 3:
                inputs.input_student_marks(school)
            case 4:
                output.list_courses(school)
            case 5:
                output.list_students(school)
            case 6:
                output.show_student_marks(school)
            case 7:
                output.show_student_gpas(school)
            case 8:
                compression.remove_data()
            case _:
                print("Invalid option!")
                continue


if __name__ == "__main__":
    main()
