import tkinter as tk
import tkinter.font as tkFont
import sqlite3
from PIL import Image , ImageTk
from tkinter import *

conn = sqlite3.connect(r"E:\project\databeta.db")     
root = tk.Tk()
root.title("SHOP")
#setting window size
width=1306
height=697
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
p = PhotoImage(file="E:\\project\\NEWNEW\\SHOP.png")
j = PhotoImage(file="E:/project/GFGUI/buynow/cart.png")
q = PhotoImage(file="E:/project/GFGUI/buynow/back.png")

GLineEdit_882=tk.Entry(root,borderwidth="1px",fg="#333333",justify="center",text="Entry")
ft = tkFont.Font(font=('Times',10))
GLineEdit_882.place(x=1590,y=270,width=70,height=25)

GLabel_80=tk.Label(root,image=p,bg="#08375b",cursor="heart",fg="#333333",justify="center")
ft = tkFont.Font(font=('Times',10))
GLabel_80.place(x=0,y=0,width=1309,height=697)

GButton_994=tk.Button(root,image=j,bg="#999999",borderwidth="4px",cursor="heart",fg="#333333",justify="center",relief="sunken")
ft = tkFont.Font(font=('Times',10))
GButton_994.place(x=1150,y=150,width=55,height=50)

GListBox_134=tk.Listbox(root,bg="#ffffff",borderwidth="8px",cursor="heart",fg="#333333",justify="center",relief="sunken")
ft = tkFont.Font(font=('Times',18))
GListBox_134.place(x=70,y=210,width=1146,height=453)

GButton_917=tk.Button(root,image=q,borderwidth="5px",cursor="heart",bg="#ffffff",fg="#000000")
GButton_917.place(x=1200,y=30,width=44,height=40)
GButton_917["command"] = root.title

if __name__ == "__main__":
    root.mainloop()
