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

registergui =toplevel.Tk()
registergui.geometry("661x470")
registergui.resizable(width=False,height=False)



entryregisterusername =toplevel.Entry(registergui,font=("Times",20),)
entryregisterusername.place(x=240,y=140,width=180,height=43)

entryregisterpassword =toplevel.Entry(registergui,font=("Times",20),show="*")
entryregisterpassword.place(x=240,y=240,width=181,height=38)



registerbutton =toplevel.Button(registergui,text="Register",font=("Times",10),command=create_user)
registerbutton.place(x=300,y=330,width=52,height=30)


registergui.mainloop()
