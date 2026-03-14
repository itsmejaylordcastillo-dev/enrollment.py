import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime


class StudentEnrollmentSystem:

    def __init__(self, frame):

        self.frame = frame
        self.connect_db()

        main = tk.Frame(self.frame, bg="#f5f7fb")
        main.pack(fill="both", expand=True, padx=10, pady=10)

        # ===== STUDENT INFORMATION PANEL =====
        input_frame = tk.LabelFrame(
            main,
            text="Student Information",
            font=("Constantia", 28, "bold"),
            bg="#ffffff",
            fg="#2c3e50",
            bd=1,
            padx=30,
            pady=30
        )
        input_frame.pack(fill="x")

        input_frame.grid_columnconfigure(0, weight=1)
        input_frame.grid_columnconfigure(2, weight=1)
        input_frame.grid_columnconfigure(3, weight=1)
        input_frame.grid_columnconfigure(4, weight=1)

        # ===== FORM FIELDS =====

        label_font = ("Segoe UI", 10, "bold")

        # Row 0
        tk.Label(input_frame, text="Student ID:", font=("Constantia", 12, "bold"), bg="#1f2a6d", fg="white").grid(row=0, column=0,
        padx=20, pady=8,sticky="e")
        self.student_id = ttk.Entry(input_frame, width=30)
        self.student_id.grid(row=0, column=1, padx=10, pady=8)

        tk.Label(input_frame, text="First Name:", font=("Constantia", 12, "bold"), bg="#1f2a6d", fg="white").grid(row=0, column=2,
         padx=20, pady=8,sticky="e")
        self.first_name = ttk.Entry(input_frame, width=30)
        self.first_name.grid(row=0, column=3, padx=10, pady=8)

        # Row 1
        tk.Label(input_frame, text="Last Name:", font=("Constantia", 12, "bold"), bg="#1f2a6d", fg="white").grid(row=1, column=0,
         padx=20, pady=8, sticky="e")
        self.last_name = ttk.Entry(input_frame, width=30)
        self.last_name.grid(row=1, column=1, padx=10, pady=8)

        tk.Label(input_frame, text="Email:", font=("Constantia", 12, "bold"), bg="#1f2a6d", fg="white").grid(row=1, column=2, padx=20, pady=8, sticky="e")
        self.email = ttk.Entry(input_frame, width=30)
        self.email.grid(row=1, column=3, padx=10, pady=8)

        # Row 2
        tk.Label(input_frame, text="Phone:", font=("Constantia", 12, "bold"), bg="#1f2a6d", fg="white").grid(row=2, column=0, padx=20,pady=8, sticky="e")
        self.phone = ttk.Entry(input_frame, width=30)
        self.phone.grid(row=2, column=1, padx=10, pady=8)

        tk.Label(input_frame, text="Course:", font=label_font, bg="#1f2a6d", fg="white").grid(row=2, column=2, padx=20,
                                                                                              pady=8, sticky="e")

        self.course = ttk.Combobox(
            input_frame,
            width=27,
            state="readonly",
            values=[
                "CPROG 1", "CPROG 2", "CPROG 3", "CPROG 4", "CPROG 5",
                "INFOT 1", "INFOT 2", "INFOT 3", "INFOT 4", "INFOT 5",
                "GEC 1", "GEC 2", "GEC 3", "GEC 4", "GEC 5",
                "GEC 6", "GEC 7", "GEC 8", "GEC 9", "GEC 10"
            ]
        )

        self.course.grid(row=2, column=3, padx=10, pady=8)

        # Row 3
        tk.Label(input_frame, text="Enrollment Date:", font=("Constantia", 12, "bold"), bg="#1f2a6d", fg="white").grid(row=3, column=0,padx=20, pady=8,sticky="e")
        self.enrollment_date = ttk.Entry(input_frame, width=30)
        self.enrollment_date.grid(row=3, column=1, padx=10, pady=8)

        self.enrollment_date.insert(0, datetime.now().strftime("%Y-%m-%d"))

        # ===== SEARCH BAR =====

        search_frame = tk.Frame(main, bg="#f0f2f5")
        search_frame.pack(fill="x", pady=5)

        tk.Label(
            search_frame,
            text="Search Student:",
            font=("Segoe UI", 10, "bold"),
            bg="#f0f2f5"
        ).pack(side="left", padx=10)

        self.search_entry = ttk.Entry(search_frame, width=30)
        self.search_entry.pack(side="left", padx=5)

        search_btn = ttk.Button(
            search_frame,
            text="Search",
            command=self.search_student
        )
        search_btn.pack(side="left", padx=5)

        show_all_btn = ttk.Button(
            search_frame,
            text="Show All",
            command=self.load_data
        )
        show_all_btn.pack(side="left", padx=5)



        #== == = TABLE == == =

        table_frame = tk.Frame(main, bg="#f0f2f5")
        table_frame.pack(fill="both", expand=True, pady=10)

        columns = ("id", "first", "last", "email", "phone", "course", "date")

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=10
        )

        # Table Style
        style = ttk.Style()
        style.configure("Treeview", rowheight=28)

        self.tree.tag_configure("odd", background="#f2f2f2")
        self.tree.tag_configure("even", background="white")

        # ===== HEADINGS =====
        self.tree.heading("id", text="Student ID")
        self.tree.heading("first", text="First Name")
        self.tree.heading("last", text="Last Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("phone", text="Phone")
        self.tree.heading("course", text="Course")
        self.tree.heading("date", text="Enrollment Date")

        # ===== COLUMN WIDTH =====
        self.tree.column("id", width=120, anchor="center")
        self.tree.column("first", width=140, anchor="center")
        self.tree.column("last", width=140, anchor="center")
        self.tree.column("email", width=200, anchor="center")
        self.tree.column("phone", width=140, anchor="center")
        self.tree.column("course", width=140, anchor="center")
        self.tree.column("date", width=150, anchor="center")

        # ===== SCROLLBAR =====
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    # ===== DATABASE =====

    def connect_db(self):

        self.conn = sqlite3.connect("students.db")
        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
        student_id TEXT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        phone TEXT,
        course TEXT,
        enrollment_date TEXT)
        """)

        self.conn.commit()

    # ===== LOAD DATA =====

    def load_data(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students")

        rows = cursor.fetchall()

        for i, row in enumerate(rows):

            if i % 2 == 0:
                self.tree.insert("", "end", values=row, tags=("even",))
            else:
                self.tree.insert("", "end", values=row, tags=("odd",))

    # ===== SEARCH STUDENT =====

    def search_student(self):

        keyword = self.search_entry.get()

        for row in self.tree.get_children():
            self.tree.delete(row)

        cursor = self.conn.cursor()

        cursor.execute("""
                       SELECT *
                       FROM students
                       WHERE student_id LIKE ?
                          OR first_name LIKE ?
                          OR last_name LIKE ?
                       """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))

        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)



    # ===== ADD STUDENT =====

    def add_student(self):

        data = (
            self.student_id.get(),
            self.first_name.get(),
            self.last_name.get(),
            self.email.get(),
            self.phone.get(),
            self.course.get(),
            self.enrollment_date.get()
        )

        if not data[0]:
            messagebox.showerror("Error", "Student ID required")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO students VALUES(?,?,?,?,?,?,?)", data)
            self.conn.commit()
            self.load_data()
            self.clear_fields()
        except:
            messagebox.showerror("Error", "Student already exists")

    # ===== UPDATE =====

    def update_student(self):

        cursor = self.conn.cursor()

        cursor.execute("""
        UPDATE students
        SET first_name=?, last_name=?, email=?, phone=?, course=?, enrollment_date=?
        WHERE student_id=?
        """, (
            self.first_name.get(),
            self.last_name.get(),
            self.email.get(),
            self.phone.get(),
            self.course.get(),
            self.enrollment_date.get(),
            self.student_id.get()
        ))

        self.conn.commit()
        self.load_data()

    # ===== DELETE =====

    def delete_student(self):

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?")

        if confirm:

            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM students WHERE student_id=?", (self.student_id.get(),))

            self.conn.commit()
            self.load_data()
            self.clear_fields()

    # ===== CLEAR =====

    def clear_fields(self):

        self.student_id.delete(0, tk.END)
        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.course.delete(0, tk.END)

    # ===== SELECT FROM TABLE =====

    def on_select(self, event):

        selected = self.tree.selection()

        if selected:

            values = self.tree.item(selected[0])["values"]

            self.student_id.delete(0, tk.END)
            self.student_id.insert(0, values[0])

            self.first_name.delete(0, tk.END)
            self.first_name.insert(0, values[1])

            self.last_name.delete(0, tk.END)
            self.last_name.insert(0, values[2])

            self.email.delete(0, tk.END)
            self.email.insert(0, values[3])

            self.phone.delete(0, tk.END)
            self.phone.insert(0, values[4])

            self.course.delete(0, tk.END)
            self.course.insert(0, values[5])

            self.enrollment_date.delete(0, tk.END)
            self.enrollment_date.insert(0, values[6])