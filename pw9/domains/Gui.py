import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from . import Student, School, Course
from Utilities import pickletool, compression


class Gui:
    def __init__(self, root, school: School):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x400")
        self.school = school

        # Tab handling
        self.notebook = ttk.Notebook(self.root, width=800, height=300)
        self.tab_student = ttk.Frame(self.notebook)
        self.tab_course = ttk.Frame(self.notebook)
        self.tab_grade = ttk.Frame(self.notebook)
        self.tab_grade_entry = ttk.Frame(self.notebook)
        self.tab_gpa = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_student, text="Students")
        self.notebook.add(self.tab_course, text="Courses")
        self.notebook.add(self.tab_grade, text="Grades")
        self.notebook.add(self.tab_grade_entry, text="Grades entry")
        self.notebook.add(self.tab_gpa, text="GPAs")

        self.notebook.pack(expand=1, fill="both")

        # Menu
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="save", command=self.savefile)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.root.config(menu=self.menubar)

        # Entry fields
        # Students
        self.student_id_label = tk.Label(self.tab_student, text="Student ID:")
        self.student_id_label.grid(row=0, column=0)
        self.student_id_entry = tk.Entry(self.tab_student)
        self.student_id_entry.grid(row=0, column=1)

        self.student_name_label = tk.Label(self.tab_student, text="Student Name:")
        self.student_name_label.grid(row=1, column=0)
        self.student_name_entry = tk.Entry(self.tab_student)
        self.student_name_entry.grid(row=1, column=1)

        self.student_dob_label = tk.Label(self.tab_student, text="Student DOB:")
        self.student_dob_label.grid(row=2, column=0)
        self.student_dob_entry = tk.Entry(self.tab_student)
        self.student_dob_entry.grid(row=2, column=1)

        # Courses
        self.course_id_label = tk.Label(self.tab_course, text="Course ID:")
        self.course_id_label.grid(row=0, column=0)
        self.course_id_entry = tk.Entry(self.tab_course)
        self.course_id_entry.grid(row=0, column=1)

        self.course_name_label = tk.Label(self.tab_course, text="Course Name:")
        self.course_name_label.grid(row=1, column=0)
        self.course_name_entry = tk.Entry(self.tab_course)
        self.course_name_entry.grid(row=1, column=1)

        # Grades
        # self.grade_label = tk.Label(root, text="Grade:")
        # self.grade_label.grid(row=2, column=0)
        # self.grade_entry = tk.Entry(root)
        # self.grade_entry.grid(row=2, column=1)
        self.course_var = tk.StringVar()
        self.course_dropdown = ttk.Combobox(self.tab_grade, textvariable=self.course_var)
        self.course_dropdown.grid(row=3, column=0, columnspan=4)
        self.course_dropdown.bind('<FocusIn>', lambda event: self.populate_course_dropdown())

        # Button to add information to list box
        self.add_button_student = tk.Button(self.tab_student, text="Add", command=lambda: self.add_student_info(school))
        self.add_button_student.grid(row=3, column=0, columnspan=2)

        self.add_button_course = tk.Button(self.tab_course, text="Add", command=lambda: self.add_course_info(school))
        self.add_button_course.grid(row=3, column=0, columnspan=2)

        self.add_button_grade = ttk.Button(self.tab_grade, text="Submit Grades", command=self.create_grade_input)
        self.add_button_grade.grid(row=4, column=0, columnspan=2)

        self.show_gpas = tk.Button(self.tab_gpa, text="Show student gpas", command=self.show_student_gpas)
        self.show_gpas.grid(row=3, column=0, columnspan=2)

        # List box to display information
        self.listbox_student = tk.Listbox(self.tab_student, width=100)
        self.listbox_student.grid(row=4, column=0, columnspan=2)

        self.listbox_course = tk.Listbox(self.tab_course, width=100)
        self.listbox_course.grid(row=4, column=0, columnspan=2)

        self.listbox_grade = tk.Listbox(self.tab_grade, width=100)
        self.listbox_grade.grid(row=6, column=0, columnspan=2)

        self.listbox_gpa = tk.Listbox(self.tab_gpa, width=100)
        self.listbox_gpa.grid(row=6, column=0, columnspan=2)

        # Check if there are any already existing data and add to list box
        if len(school.getstudents()) > 0:
            for student in school.getstudents():
                self.listbox_student.insert(tk.END, f"ID: {student.getid()}, Name: {student.getname()}, "
                                                    f"DOB: {student.getdob()}")

        if len(school.getcourses()) > 0:
            for course in school.getcourses():
                self.listbox_course.insert(tk.END, f"Course ID: {course.getid()}, Course Name: {course.getname()}")

        if not school.getcourses() or not school.getstudents():
            pass
        else:
            for student in school.getstudents():
                for course in student.getmark():
                    self.listbox_grade.insert(tk.END, f"Student {student.getid()}, course {course}:"
                                                      f" {student.getmark().get(course, 'Not enrolled')}")

    def add_student_info(self, school: School):
        student_name = self.student_name_entry.get()
        student_dob = self.student_dob_entry.get()
        student_id = self.student_id_entry.get()

        if not student_name or not student_dob or not student_id:
            messagebox.showerror("Error", "Please fill in all fields and try again.")
            return

        school.add_student(Student.Student(student_id, student_name, student_dob))

        self.listbox_student.insert(tk.END, f"ID: {student_id}, Name: {student_name}, DOB: {student_dob}")
        self.student_name_entry.delete(0, tk.END)
        self.student_id_entry.delete(0, tk.END)
        self.student_dob_entry.delete(0, tk.END)

    def add_course_info(self, school: School):
        course_name = self.course_name_entry.get()
        course_id = self.course_id_entry.get()

        if not course_name or not course_id:
            messagebox.showerror("Error", "Please fill in all fields and try again.")
            return

        school.add_course(Course.Course(course_id, course_name))

        self.listbox_course.insert(tk.END, f"Course ID: {course_id}, Course Name: {course_name}")
        self.course_name_entry.delete(0, tk.END)
        self.course_id_entry.delete(0, tk.END)

    # populate dropdown menu with courses
    def populate_course_dropdown(self):
        courses = self.school.getcourses()
        course_ids = [course.getid() for course in courses]
        self.course_dropdown['values'] = course_ids

    def create_grade_input(self):
        for widget in self.tab_grade_entry.winfo_children():
            widget.destroy()

        self.grade_entries = []

        for student in self.school.getstudents():
            label = ttk.Label(self.tab_grade_entry, text=student.getname())
            # label.grid(row=2, column=3)
            label.pack()
            entry = ttk.Entry(self.tab_grade_entry)
            # entry.grid(row=3, column=3)
            entry.pack()
            self.grade_entries.append(entry)

        self.add_button_grade_entry = ttk.Button(self.tab_grade_entry, text="Add", command=self.submit_grades)
        # self.add_button_grade_entry.grid(row=4, column=0, columnspan=2)
        self.add_button_grade_entry.pack()

    def submit_grades(self):
        selected_course = self.course_var.get()
        grades = [entry.get() for entry in self.grade_entries]
        for student, grade in zip(self.school.getstudents(), grades):
            student.add_mark(selected_course, float(grade))

            # add entered grades to grade tab
            self.listbox_grade.insert(tk.END, f"Student {student.getid()}, course {selected_course}:"
                                              f" {grade}")

    def show_student_gpas(self):
        self.listbox_gpa.delete(0, tk.END)

        if not self.school.getcourses() or not self.school.getstudents():
            return

        # print("\nUnsorted:")
        self.listbox_gpa.insert(tk.END, f"Unsorted:")
        for student in self.school.getstudents():
            self.listbox_gpa.insert(tk.END, f"Student {student.getid()}: {self.school.calculate_average_gpa(student)}")
            # print(f"Student {student.getid()}: {self.school.calculate_average_gpa(student)}")

        gpas = {student.getid(): self.school.calculate_average_gpa(student)
                for student in self.school.getstudents()}
        sorted_gpas = sorted(gpas.items(), key=lambda x: x[1], reverse=True)
        # print("\nGPA from highest to lowest:")
        self.listbox_gpa.insert(tk.END, "GPA from highest to lowest:")
        for student_id, gpa in sorted_gpas:
            self.listbox_gpa.insert(tk.END, f"Student {student_id}: {gpa}")
            # print(f"Student {student_id}: {gpa}")

    def savefile(self):
        save_thread = threading.Thread(target=pickletool.storeData, args=(self.school,))
        save_thread.start()
        save_thread.join()
        compression.compress()