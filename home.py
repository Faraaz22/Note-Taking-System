import tkinter as tk
from tkinter import messagebox, filedialog
import mysql.connector
from tkinter import Menu


def return_to_login():
    root.destroy()
    import main


def return_to_register():
    root.destroy()
    import register


def save_on_device():
    open_file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if open_file is None:
        return

    try:
        with open(open_file, "w") as file:
            file.write(entry.get(1.0, tk.END))
        messagebox.showinfo("Success", "Note saved to file successfully!")

    except (IOError, PermissionError) as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return


def save_note():
    note_text = entry.get(1.0, tk.END)

    try:
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="1234", database="notes"
        )
        mycursor = mydb.cursor()

    except (IOError, PermissionError) as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return

    query = "insert into notes(id,note) values(%s, %s)"
    mycursor.execute(query, (None, note_text))

    mydb.commit()
    mydb.close()
    messagebox.showinfo("Success", "Note saved to database successfully!")


def open_note():
    """Opens an existing text file and displays its content in the entry box."""
    open_file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )
    if open_file is None:
        return

    try:
        with open(open_file, "r") as file:
            content = file.read()
        entry.delete(1.0, tk.END)  # Clear existing content
        entry.insert(tk.INSERT, content)
    except (IOError, PermissionError) as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def clear_entry():
    """Clears the contents of the text entry widget."""
    entry.delete(1.0, tk.END)


root = tk.Tk()
root.title("Notepad")
root.geometry("600x600")

root.config(bg="#f5f5f5")  # Light gray

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save As...", command=save_note)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
returnmenu = Menu(menubar, tearoff=0)
returnmenu.add_command(label="Return to Login Page", command=return_to_login)
returnmenu.add_command(label="Go to Register Page", command=return_to_register)
menubar.add_cascade(label="Return", menu=returnmenu)
root.config(menu=menubar)

head_label = tk.Label(root, text="Enter Your Note:", font=("Arial", 25, "bold"))
head_label.place(x=5, y=5)
# Create clear and concise button labels
button_save = tk.Button(
    root, width=20, height=2, text="Save Note", command=save_note
)
button_save.place(x=1000, y=100)

button_open = tk.Button(
    root, width=20, height=2, text="Open Note", command=open_note
)
button_open.place(x=1000, y=250)

button_clear = tk.Button(
    root, width=20, height=2, text="Clear", command=clear_entry
)
button_clear.place(x=1000, y=400)  # Adjust placement as needed
button_save_2 = tk.Button(
    root, width=20, height=2, text="Save on system", command=save_on_device
)
button_save_2.place(x=1000, y=550)

# Create a spacious and user-friendly text entry widget
entry = tk.Text(root, height=33, width=72, wrap=tk.WORD, font=("Arial", 14))
entry.place(x=10, y=60)

# Ensure clean and organized layout with padding
entry.config(padx=10, pady=10, highlightthickness=0)  # Remove default border

root.mainloop()
