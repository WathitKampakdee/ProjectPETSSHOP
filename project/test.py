import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import random
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from datetime import datetime
from tkinter import messagebox
import tkinter as toplevel
conn = sqlite3.connect(r"E:\project\databeta.db")
cursor = conn.cursor()
def loginadmin():
    def get_usernamepassword():
        username_login=e1.get()
        password_login=e2.get()
        cursor.execute("SELECT uesr, password FROM adminid WHERE uesr=? and password=?", (username_login, password_login))
        user_data = cursor.fetchone()
        if user_data:
            username, password = user_data
            print(user_data)
            dd.destroy()
            
        else:
            return None, None  


    def create_user():
        x = e1.get()
        y = e2.get()
        if x.lower() == "admin":
            messagebox.showinfo(title=None,message="ใช้ชื่อนี้ไม่ได้")
        elif not x:
            messagebox.showinfo(title=None,message="ใส่ข้อมูลให้ครบ")
        else:
            cursor.execute("INSERT INTO adminid (uesr, password) VALUES (?, ?)", (x, y))
            e1.delete(0,tk.END)
            e2.delete(0,tk.END)
            
            conn.commit()
            messagebox.showinfo(title=None,message=f"{x}บัญชีผู้ใช้ถูกสร้างเรียบร้อยแล้ว")
        conn.close()
        dd.destroy()
    
    dd =toplevel.Tk()
    dd.geometry("661x470")
    dd.resizable(width=False,height=False)



    e1 =toplevel.Entry(dd,font=("Times",20),)
    e1.place(x=240,y=140,width=180,height=43)

    e2 =toplevel.Entry(dd,font=("Times",20),show="*")
    e2.place(x=240,y=240,width=181,height=38)



    registerbutton =toplevel.Button(dd,text="log",font=("Times",10),command=get_usernamepassword)
    registerbutton.place(x=300,y=330,width=52,height=30)
    rebutton =toplevel.Button(dd,text="register",font=("Times",10),command=create_user)
    rebutton.place(x=400,y=330,width=52,height=30)



    dd.mainloop()