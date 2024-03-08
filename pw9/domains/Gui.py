import tkinter as tk
from tkinter import messagebox
import threading
from . import Course, Student, School
from Utilities import *


class Gui:
    def __init__(self, root, school: School):
        self.root = root
        self.root.title("Student Management System")
        self.school = school

        # Menu
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="save", command = self.savefile)
        self.menubar.add_cascade(label="File", menu = self.filemenu)

        self.root.config(menu=self.menubar)

        # Entry fields
        self.student_id_label = tk.Label(root, text="Student ID:")
        self.student_id_label.grid(row=0, column=0)
        self.student_id_entry = tk.Entry(root)
        self.student_id_entry.grid(row=0, column=1)

        self.student_name_label = tk.Label(root, text="Student Name:")
        self.student_name_label.grid(row=1, column=0)
        self.student_name_entry = tk.Entry(root)
        self.student_name_entry.grid(row=1, column=1)

        self.student_dob_label = tk.Label(root, text="Student DOB:")
        self.student_dob_label.grid(row=2, column=0)
        self.student_dob_entry = tk.Entry(root)
        self.student_dob_entry.grid(row=2, column=1)

        # self.course_id_label = tk.Label(root, text="Course Name:")
        # self.course_id_label.grid(row=1, column=0)
        # self.course_id_entry = tk.Entry(root)
        # self.course_id_entry.grid(row=1, column=1)
        #
        # self.course_name_label = tk.Label(root, text="Course Name:")
        # self.course_name_label.grid(row=1, column=0)
        # self.course_name_entry = tk.Entry(root)
        # self.course_name_entry.grid(row=1, column=1)

        # self.grade_label = tk.Label(root, text="Grade:")
        # self.grade_label.grid(row=2, column=0)
        # self.grade_entry = tk.Entry(root)
        # self.grade_entry.grid(row=2, column=1)

        # Button to add information to list box
        self.add_button = tk.Button(root, text="Add", command= lambda: self.add_student_info(school))
        self.add_button.grid(row=3, column=0, columnspan=2)

        # List box to display information
        self.listbox = tk.Listbox(root, width=100)
        self.listbox.grid(row=4, column=0, columnspan=2)

        if len(school.getstudents()) > 0:
            for student in school.getstudents():
                self.listbox.insert(tk.END, f"ID: {student.getid()}, Name: {student.getname()}, DOB: {student.getdob()}")

    def add_student_info(self, school: School):
        student_name = self.student_name_entry.get()
        student_dob = self.student_dob_entry.get()
        student_id = self.student_id_entry.get()

        if not student_name or not student_dob or not student_id:
            messagebox.showerror("Error", "Please fill in all fields and try again.")
            return

        school.add_student(Student.Student(student_id, student_name, student_dob))

        self.listbox.insert(tk.END, f"ID: {student_id}, Name: {student_dob}, DOB: {student_name}")
        self.student_name_entry.delete(0, tk.END)
        self.student_id_entry.delete(0, tk.END)
        self.student_dob_entry.delete(0, tk.END)

    def savefile(self):
        save_thread = threading.Thread(target=pickletool.storeData, args=(self.school,))
        save_thread.start()
        save_thread.join()
        compression.compress()
