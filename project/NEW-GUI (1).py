import tkinter as tk
import tkinter.font as tkFont
import sqlite3
from PIL import Image, ImageTk
from tkinter import *

conn = sqlite3.connect(r"E:\project\databeta.db")      
root = tk.Tk()
root.title("CLASSY STORE")
#setting window size
width=1306
height=697
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
r = PhotoImage(file="E:\\project\\NEWNEW\\\CLASSYYY.png")
e = PhotoImage(file="E:\project\GFGUI\homepage\Cr.png")

bgorder = Label(root,image=r,cursor="heart")
bgorder.place(x=0, y=0, width=1306, height=697)

GButton_737=tk.Button(root,bg="#ffffff",borderwidth="5px",cursor="heart",fg="#000000",justify="center",text="SHOP NOW",relief="sunken")
ft = tkFont.Font(font=('Times',18))
GButton_737.place(x=550,y=260,width=206,height=64)
GButton_737["command"] = root.title

GButton_23=tk.Button(root,bg="#ffffff",borderwidth="5px",cursor="heart",fg="#000000",justify="center",relief="sunken",text="ADMIN")
ft = tkFont.Font(font=('Times',18))
GButton_23.place(x=550,y=360,width=206,height=64)

GButton_741=tk.Button(root,bg="#ffffff",borderwidth="5px",cursor="heart",fg="#000000",justify="center",text="CLOSE",relief="sunken")
ft = tkFont.Font(font=('Times',18))
GButton_741.place(x=550,y=460,width=206,height=64)

GButton_917=tk.Button(root,image=e)
GButton_917["borderwidth"] = "5px"
GButton_917.place(x=1250,y=30,width=44,height=40)


root.mainloop()