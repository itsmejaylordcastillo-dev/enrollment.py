import tkinter as tk
from tkinter import messagebox
from dashboard import Dashboard


class LoginSystem:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Enrollment System - Login")
        self.root.geometry("500x400")
        self.root.configure(bg="#f5f7fb")
        self.root.resizable(False, False)

        # ===== MAIN FRAME =====
        main = tk.Frame(root, bg="#f5f7fb")
        main.pack(expand=True)

        # ===== LOGIN CARD =====
        card = tk.Frame(main, bg="white", padx=40, pady=40)
        card.pack()

        # ===== TITLE =====
        tk.Label(
            card,
            text="Student Enrollment System",
            font=("Segoe UI", 18, "bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(pady=(0, 20))

        tk.Label(
            card,
            text="Login",
            font=("Segoe UI", 14),
            bg="white",
            fg="#555"
        ).pack(pady=(0, 20))

        # ===== USERNAME =====
        tk.Label(
            card,
            text="Username",
            font=("Segoe UI", 10),
            bg="white"
        ).pack(anchor="w")

        self.username = tk.Entry(card, font=("Segoe UI", 11), width=25)
        self.username.pack(pady=5)

        # ===== PASSWORD =====
        tk.Label(
            card,
            text="Password",
            font=("Segoe UI", 10),
            bg="white"
        ).pack(anchor="w")

        self.password = tk.Entry(card, show="*", font=("Segoe UI", 11), width=25)
        self.password.pack(pady=5)

        # ===== LOGIN BUTTON =====
        tk.Button(
            card,
            text="Login",
            font=("Segoe UI", 11, "bold"),
            bg="#4a6cf7",
            fg="white",
            width=20,
            bd=0,
            pady=8,
            command=self.login
        ).pack(pady=20)

    # ===== LOGIN FUNCTION =====
    def login(self):

        user = self.username.get()
        pwd = self.password.get()

        if user == "admin" and pwd == "admin123":

            # Close login window
            self.root.destroy()

            # Open dashboard
            dashboard_window = tk.Tk()
            Dashboard(dashboard_window)
            dashboard_window.mainloop()

        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


# ===== RUN LOGIN =====
if __name__ == "__main__":

    root = tk.Tk()
    LoginSystem(root)
    root.mainloop()