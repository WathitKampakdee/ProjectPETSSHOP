import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

# เชื่อมต่อกับฐานข้อมูล
conn = sqlite3.connect(r"E:\project\login.db")
cursor = conn.cursor()

# ฟังก์ชันการเข้ารหัสรหัสผ่าน
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(username, password):
    hashed_password = hash_password(password)
    cursor.execute('INSERT INTO admin (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()

def add_user_gui():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        add_user(username, password)
        messagebox.showinfo('เพิ่มผู้ใช้', 'เพิ่มผู้ใช้เรียบร้อยแล้ว!')

    else:
        messagebox.showerror('ข้อผิดพลาด', 'โปรดป้อนชื่อผู้ใช้และรหัสผ่านทั้งคู่.')
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# ตรวจสอบการลงชื่อเข้าใช้
def login():
    username = username_entry.get()
    password = password_entry.get()

    hashed_password = hash_password(password)
    cursor.execute('SELECT password FROM admin WHERE username = ?', (username,))
    result = cursor.fetchone()
    if result and result[0] == hashed_password:
        messagebox.showinfo('Login', 'Login successful!')
        logingui.destroy()
    else:
        messagebox.showerror('Login', 'Invalid credentials.')
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# ฟังก์ชันเพื่อดำเนินการเมื่อปิดหน้าต่าง
def on_closing():
    conn.close()
    logingui.destroy()

# สร้าง GUI
logingui = tk.Tk()
logingui.title('Login System')

frame = tk.Frame(logingui)
frame.pack(padx=20, pady=20)

tk.Label(frame, text='Username:').grid(row=0, column=0, pady=(0, 10))
username_entry = tk.Entry(frame)
username_entry.grid(row=0, column=1, pady=(0, 10))

tk.Label(frame, text='Password:').grid(row=1, column=0, pady=(0, 10))
password_entry = tk.Entry(frame, show='*')
password_entry.grid(row=1, column=1, pady=(0, 10))

# Button to add a user
add_user_button = tk.Button(frame, text='Add User', command=add_user_gui)
add_user_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))

# Button to perform login
login_button = tk.Button(frame, text='Login', command=login)
login_button.grid(row=4, column=0, columnspan=2, pady=(10, 0))

# Button to exit the application
exit_button = tk.Button(frame, text='Exit', command=on_closing)
exit_button.grid(row=5, column=0, columnspan=2, pady=(10, 0))

logingui.mainloop()