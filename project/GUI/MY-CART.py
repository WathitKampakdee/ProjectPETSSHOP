import tkinter as tk
import tkinter.font as tkFont
import sqlite3
from PIL import Image, ImageTk
from tkinter import *

conn = sqlite3.connect(r"D:\Python\DB\Project\final.db")      
root = tk.Tk()
root.title("My cart")
#setting window size
width=1013
height=760
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
r = PhotoImage(file="D:\Python\DB\Project\image BG\ROSE.png")
c = PhotoImage(file="D:\Python\DB\Project\image BG\close.png")
e = PhotoImage(file="D:\Python\DB\Project\Button\EDIT P CART.png")
p = PhotoImage(file="D:\Python\DB\Project\Button\PAY P CART.png")


bgorder = Label(root,image=r,cursor="heart")
bgorder.place(x=0, y=0, width=1020, height=730)


GButton_298=tk.Button(root,image=c)
GButton_298.place(x=960,y=10,width=30,height=35)

GLabel_232=tk.Label(root)
GLabel_232["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=10)
GLabel_232["font"] = ft
GLabel_232["fg"] = "#333333"
GLabel_232["justify"] = "center"
GLabel_232["text"] = ""
GLabel_232.place(x=50,y=60,width=910,height=586)

GLabel_786=tk.Label(root)
ft = tkFont.Font(family='Times',size=30)
GLabel_786["font"] = ft
GLabel_786["bg"] = "#000000"
GLabel_786["fg"] = "#ffffff"
GLabel_786["justify"] = "center"
GLabel_786["text"] = "YOUR CART"
GLabel_786.place(x=320,y=100,width=379,height=40)

GButton_797=tk.Button(root,image=e)
GButton_797["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=10)
GButton_797["font"] = ft
GButton_797["fg"] = "#ffffff"
GButton_797["justify"] = "center"
GButton_797["text"] = "EDIT"
GButton_797.place(x=240,y=670,width=211,height=47)

GButton_617=tk.Button(root,image=p)
GButton_617["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=10)
GButton_617["font"] = ft
GButton_617["fg"] = "#ffffff"
GButton_617["justify"] = "center"
GButton_617["text"] = "PAY"
GButton_617.place(x=560,y=670,width=211,height=47)



root.mainloop()