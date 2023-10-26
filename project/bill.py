import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import sqlite3
from tkinter import filedialog
import io
from PIL import Image, ImageTk
from tkinter import *
from io import BytesIO
from datetime import datetime
from tkinter import messagebox


now = datetime.today()
conn=sqlite3.connect(r"E:\project\databeta.db")
cursor = conn.cursor()
def cash():
    c = conn.cursor()
    c.execute('''SELECT * FROM myorder''')
    result = c.fetchall()
    date=now
    category="sales,cash"
    for x in result:
        namehistory,pricehistory,quantity=x[1],x[2],x[3]
        print(category,"  /  ",namehistory,"  /  ",pricehistory,"  /  ",quantity,"  /  ",date)
        if category and namehistory and pricehistory and quantity and date :
            cursor.execute("INSERT INTO history (category,name,price,quantity,date) VALUES (?, ?, ?, ?, ?)", (category,namehistory,pricehistory,quantity,date))
            conn.commit()
        cursor.execute("DELETE FROM myorder")
        conn.commit()
def transferpayment():
    messagebox.askquestion("แน่ใจมั้ย", "ต้องโอนเงินนะ?")
    c = conn.cursor()
    c.execute('''SELECT * FROM myorder''')
    result = c.fetchall()
    date=now
    category="sales,transfer payment"
    for x in result:
        namehistory,pricehistory,quantity=x[1],x[2],x[3]
        print(category,"  /  ",namehistory,"  /  ",pricehistory,"  /  ",quantity,"  /  ",date)
        if category and namehistory and pricehistory and quantity and date :
            cursor.execute("INSERT INTO history (category,name,price,quantity,date) VALUES (?, ?, ?, ?, ?)", (category,namehistory,pricehistory,quantity,date))
            conn.commit()
        cursor.execute("DELETE FROM myorder")
        conn.commit()

    

def back():
    print("...")       
  
bill = tk.Tk()
bill.title("MANU_ADMIN")
width=1019
height=730
screenwidth = bill.winfo_screenwidth()
screenheight = bill.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
bill.geometry(alignstr)
bill.resizable(width=False, height=False)
r = PhotoImage(file="E:\project\IMAGE BG\ROSE.png")
f = PhotoImage(file="E:\project\BUTTON\FFF.png")
ff = PhotoImage(file="E:\project\BUTTON\FFF2.png")
fff = PhotoImage(file="E:\project\BUTTON\FFF3.png")
bg_color=tk.Label(bill,image=r)
bg_color.place(x=0,y=0,width=1019,height=725)

c = PhotoImage(file="E:\project\IMAGE BG\CLASSY.png")

namestore=Label(bill,image=c, borderwidth="3px",cursor="heart", justify="center", relief="sunken")
namestore.place(x=100,y=7,width=498,height=66)


delete_button = tk.Button(bill, bg="#F9DEC9", cursor="heart", font=("Times", 17), fg="#000000", justify="center", text="cash", borderwidth="3px",command=cash)
delete_button.place(x=400, y=670, width=80, height=40)


edit_button = tk.Button(bill, bg="#F9DEC9", cursor="heart",font=("Times", 17), fg="#000000", justify="center", text="Transfer payment", borderwidth="3px",command=transferpayment)
edit_button.place(x=130, y=670, width=250, height=40)


products_listbox = tk.Listbox(bill, bg="#ffffff", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
products_listbox.place(x=20, y=80, width=600, height=579)



end = tk.Button(bill, bg="#ff0000", font=("Times", 20), justify="center", text="X", borderwidth="3px", command=back)
end.place(x=940, y=17, width=50, height=50)
bill.mainloop()