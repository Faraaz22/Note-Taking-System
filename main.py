import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from pyasn1_modules.rfc7906 import Register
from tkinter import messagebox
import random
from tkcalendar import DateEntry
from datetime import datetime

import mysql.connector

root = tk.Tk()
root.title("Login Page")
# ------------------------LOGIN PAGE START
# Configure window size and padding
root.geometry("300x200")
root.configure(padx=20, pady=20)
PASSWORD = "1234"

# Create a frame for login elements
login_frame = tk.Frame(root, bg="lightblue", relief="raised", bd=2)
login_frame.pack(fill="both", expand=True)

# Username label and entry
username_label = tk.Label(login_frame, text="Username:", font=("Arial", 12))
username_label.pack(pady=5)


def user_enter(e):
    username_entry.delete(0, 'end')


def user_leave(e):
    name = username_entry.get()
    if name == '':
        username_entry.insert(0, 'UserID')


username_entry = tk.Entry(login_frame, font=("Arial", 12))
username_entry.insert(0, 'UserID')
username_entry.bind("<FocusIn>", user_enter)
username_entry.bind("<FocusOut>", user_leave)
username_entry.pack(pady=5)

# Password label and entry
password_label = tk.Label(login_frame, text="Password:", font=("Arial", 12))
password_label.pack(pady=5)


def password_enter(e):
    password_entry.delete(0, 'end')


def password_leave(e):
    if password_entry.get() == '':
        password_entry.insert(0, 'Password')


password_entry = tk.Entry(login_frame, show="*", font=("Arial", 12))
password_entry.insert(0, 'Password')
password_entry.bind("<FocusIn>", password_enter)
password_entry.bind("<FocusOut>", password_leave)
password_entry.pack(pady=5)


def trial():
    global trial_no
    trial_no += 1
    print("trial no is", trial_no)
    if trial_no == 3:
        messagebox.showwarning("Warning", "You have tried more")
        root.destroy()


# Login button
def loginuser():
    username = username_entry.get()
    password = password_entry.get()
    print(username, password)

    if (username == "" or username == "UserID") or (password == "" or password == "Password"):
        messagebox.showerror("Enrty error", "Type username or password")
    else:
        try:
            mydb = mysql.connector.connect(host='localhost', user='root', password=PASSWORD, database='registration')
            mycursor = mydb.cursor()
            print("Connected to Database")
        except:
            messagebox.showerror("Connection", "Couldn't connect")
            return
        command = "use registration"
        mycursor.execute(command)

        command = "select * from login where Username=%s and Password=%s"
        mycursor.execute(command, (username, password))
        myresult = mycursor.fetchone()
        print(myresult)

        if myresult == None:
            messagebox.showinfo("invalid", "Invalid userid and password")
            trial()
        else:
            messagebox.showinfo("Login", "Sucessfully Login")
            root.destroy()
            import home


login_button = tk.Button(login_frame, text="Login", command=loginuser, font=("Arial", 12))
login_button.pack(pady=10)

# Login status label
login_status_label = tk.Label(login_frame, text="", font=("Arial", 12))
login_status_label.pack()


def open_new_page():
    root.destroy()  # Destroy the previous window (main window in this case)
    import register


register_button = tk.Button(
    login_frame, text="Register", font=("Arial", 12), command=open_new_page,
)
register_button.pack(pady=5)
# --------------------------LOGIN PAGE END

root.mainloop()
