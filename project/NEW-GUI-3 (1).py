import tkinter as tk
import tkinter.font as tkFont
import sqlite3
from PIL import Image, ImageTk
from tkinter import *

conn = sqlite3.connect(r"E:\project\databeta.db") 
root = tk.Tk()
root.title("ADMIN")
#setting window size
width=1306
height=697
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
a = PhotoImage(file="E:\\project\\NEWNEW\\ADMINN.png")
y = PhotoImage(file="E:\\project\\GFGUI\\Admin\\add.png")
x = PhotoImage(file="E:\\project\\GFGUI\\Admin\\delete.png")
w = PhotoImage(file="E:\\project\\GFGUI\\Admin\\edit.png")


GLineEdit_882=tk.Entry(root,borderwidth="1px",fg="#333333",justify = "center",text = "Entry")
ft = tkFont.Font(font=('Times',10))
GLineEdit_882.place(x=1590,y=270,width=70,height=25)

GLabel_80=tk.Label(root,image=a,bg = "#08375b", cursor="heart",fg="#333333",justify="center")
ft = tkFont.Font(font=('Times',10))
GLabel_80.place(x=0,y=0,width=1309,height=697)

GLabel_55=tk.Label(root,bg="#FCCEAA",borderwidth="5px",cursor="heart",fg="#333333",justify="center",text="PRODUCT NAME",relief="sunken")
ft = tkFont.Font(family='Times',size=18)
GLabel_55.place(x=550,y=80,width=259,height=50)

GLabel_115=tk.Label(root,bg="#FCCEAA",borderwidth="5px",cursor="heart",fg="#333333",justify="center",text="PRODUCT PRICT",relief="sunken")
ft = tkFont.Font(font=('Times',18))
GLabel_115.place(x=550,y=170,width=259,height=50)

GLabel_728=tk.Label(root,bg="#FCCEAA",borderwidth="5px",cursor="heart",fg="#333333",justify="center",text="QUANTITY",relief="sunken")
ft = tkFont.Font(font=('Times',18))
GLabel_728.place(x=550,y=260,width=259,height=50)

GLineEdit_562=tk.Entry(root,bg="#ffffff",borderwidth="5px",cursor="heart",fg="#333333",justify="center",relief="sunken")
ft = tkFont.Font(font=('Times',18))
GLineEdit_562.place(x=840,y=80,width=259,height=50)

GLineEdit_795=tk.Entry(root,bg="#ffffff",borderwidth="5px",cursor="heart",fg="#333333",justify="center",relief="sunken")
ft = tkFont.Font(font=('Times',18))
GLineEdit_795.place(x=840,y=170,width=259,height=50)

GLineEdit_423=tk.Entry(root,bg="#ffffff",borderwidth="5px",cursor="heart",fg="#333333",justify="center",relief="sunken")
ft = tkFont.Font(font=('Times',18))
GLineEdit_423.place(x=840,y=260,width=259,height=50)

GBoutton_994=tk.Button(root,image=y,bg="#999999",borderwidth="2px",cursor="heart",fg="#333333",justify="center",relief="sunken")
ft = tkFont.Font(font=('Times',10))
GBoutton_994.place(x=1120,y=80,width=55,height=50)

GBtton_793=tk.Button(root,image=x,bg="#999999",borderwidth="2px",cursor="heart",fg="#333333",justify="center",relief="sunken")
ft = tkFont.Font(font=('Times',10))
GBtton_793.place(x=1120,y=170,width=55,height=50)

GButton_92=tk.Button(root,image=w,bg="#999999",borderwidth="2px",cursor="heart",fg="#333333",justify="center",relief="sunken")
ft = tkFont.Font(font=('Times',10))
GButton_92.place(x=1120,y=260,width=55,height=50)

GListBox_134=tk.Listbox(root,bg="#ffffff",borderwidth="10px",cursor="heart",fg="#333333",justify="center",relief="sunken")
ft = tkFont.Font(font=('Times',18))
GListBox_134.place(x=20,y=360,width=1269,height=314)
if __name__ == "__main__":

    root.mainloop()
