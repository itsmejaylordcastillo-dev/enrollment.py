import tkinter as tk
from enrollment import StudentEnrollmentSystem


class Dashboard:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Enrollment System")
        self.root.geometry("1100x650")
        self.root.configure(bg="#f0f2f5")

        # ===== LEFT SIDEBAR =====
        sidebar = tk.Frame(self.root, bg="#1f2a6d", width=250)
        sidebar.pack_propagate(False)
        sidebar.pack(side="left", fill="y")

        title = tk.Label(
            sidebar,
            text="DASHBOARD",
            bg="#1f2a6d",
            fg="white",
            font=("Constantia", 25, "bold")
        )
        title.pack(pady=5)

        subtitle = tk.Label(
            sidebar,
            text="ENROLLMENT SYSTEM",
            bg="#1f2a6d",
            fg="white",
            font=("Constantia", 16, "bold")
        )
        subtitle.pack(pady=5)

        # ===== MAIN CONTENT =====
        content = tk.Frame(self.root, bg="#f0f2f5")
        content.pack(side="right", fill="both", expand=True)

        app = StudentEnrollmentSystem(content)

        # ===== SIDEBAR BUTTONS =====
        btn_add = tk.Button(
            sidebar,
            text="ADD STUDENT",
            bg="#2ecc71",
            fg="white",
            font=("Constantia", 10, "bold"),
            width=22,
            command=app.add_student
        )
        btn_add.pack(pady=(90, 6))

        btn_update = tk.Button(
            sidebar,
            text="UPDATE STUDENT",
            bg="#3498db",
            fg="white",
            font=("Constantia", 10, "bold"),
            width=22,
            command=app.update_student
        )
        btn_update.pack(pady=6)

        btn_clear = tk.Button(
            sidebar,
            text="CLEAR FIELDS",
            bg="#3498db",
            fg="white",
            font=("Constantia", 10, "bold"),
            width=22,
            command=app.clear_fields
        )
        btn_clear.pack(pady=6)

        btn_refresh = tk.Button(
            sidebar,
            text="REFRESH DATA",
            bg="#3498db",
            fg="white",
            font=("Constantia", 10, "bold"),
            width=22,
            command=app.load_data
        )
        btn_refresh.pack(pady=6)

        btn_delete = tk.Button(
            sidebar,
            text="DELETE STUDENT",
            bg="#e74c3c",
            fg="white",
            font=("Constantia", 10, "bold"),
            width=22,
            command=app.delete_student
        )
        btn_delete.pack(pady=6)

        # ===== LOGOUT BUTTON =====
        logout = tk.Button(
            sidebar,
            text="LOG OUT",
            bg="#d9534f",
            fg="white",
            font=("Constantia", 15, "bold"),
            width=22,
            command=self.root.destroy
        )
        logout.pack(side="bottom", pady=6)


# Only runs if dashboard.py is opened directly
if __name__ == "__main__":
    root = tk.Tk()
    Dashboard(root)
    root.mainloop()