import tkinter as tk
from tkinter import messagebox

# Preset credentials
admin_USERNAME = ["gavin", "jose", "benedict", "emmet"]
admin_PASSWORD = ["gavin1", "jose1", "benedict1", "emmet1"]

# Function to validate login
def validate_login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Check if the username and password are valid
    if username in admin_USERNAME and password in admin_PASSWORD:
        user_index = admin_USERNAME.index(username)
        # Check if the password matches the username by index
        if admin_PASSWORD[user_index] == password:
            open_menu(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")
    else:
        messagebox.showerror("Error", "Invalid username or password")




# Function to open the menu screen
def open_menu(username):
    login_window.destroy()  # Close login window

    menu_window = tk.Tk()
    menu_window.title("Menu")

    tk.Button(menu_window, text="Admin", command=lambda: messagebox.showinfo("Admin", "Admin Page")).pack(pady=10)
    tk.Button(menu_window, text="Twitter", command=lambda: messagebox.showinfo("Twitter", "Twitter Page")).pack(pady=10)
    tk.Button(menu_window, text="Messaging", command=lambda: messagebox.showinfo("Messaging", "Messaging Page")).pack(pady=10)

    menu_window.mainloop()

# Main login screen
login_window = tk.Tk()
login_window.title("Login Screen")

tk.Label(login_window, text="Username").pack(pady=5)
entry_username = tk.Entry(login_window)
entry_username.pack(pady=5)

tk.Label(login_window, text="Password").pack(pady=5)
entry_password = tk.Entry(login_window, show="*")
entry_password.pack(pady=5)

tk.Button(login_window, text="Login", command=validate_login).pack(pady=20)

login_window.mainloop()
