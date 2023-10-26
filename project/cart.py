import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import sqlite3
from tkinter import filedialog
import io
from PIL import Image, ImageTk
from tkinter import *
from io import BytesIO
conn=sqlite3.connect(r"E:\project\databeta.db")
cursor = conn.cursor()
def checkint(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False  
tempidincart=[]
totalpriceincart=[]       
def edit():
    selected_product = products_listbox.curselection()
    if selected_product:
        a = selected_product[0]
        idedit = tempidincart[a]
        quantityproduct = quantity.get()
        cursor.execute('''UPDATE myorder SET quantity=? WHERE id =? ''',(quantityproduct,idedit))
        quantity.delete(0, tk.END)
        conn.commit()
        show()


def delete():
    selected_product = products_listbox.curselection()
    if selected_product:
        a = selected_product[0]
        product_id = tempidincart[a]
        cursor.execute("DELETE FROM myorder WHERE id=?", (product_id,))
        conn.commit()
        show()       

def show():
    products_listbox.delete(0, tk.END)
    price_listbox.delete(0, tk.END)
    q_listbox.delete(0, tk.END)
    c = conn.cursor()
    c.execute('''SELECT * FROM myorder''')
    result = c.fetchall()
    i = 1
    tempidincart.clear()
    totalpriceincart.clear() 
    sumtotal=0
    for x in result:
        products_listbox.insert(x[0]," Product No:  {}    {}    {}   {}    ".format(i,x[1],x[2],x[3]))
        tempidincart.append(x[0])
        totalpriceincart.append(x[2])
        i+=1  
        sumtotal+= x[2]*x[3]
    for y in result:
        price_listbox.insert(y[0],"        {}   THB".format(y[2]*y[3]))
    for y in result:
        q_listbox.insert(y[0]," ▶  {}  ".format(y[3]))    
    print(sumtotal)
    


               

      
def back():
    cartfram.destroy()       
        
cartfram = tk.Tk()
cartfram.title("MANU_ADMIN")
width=1019
height=730
screenwidth = cartfram.winfo_screenwidth()
screenheight = cartfram.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
cartfram.geometry(alignstr)
cartfram.resizable(width=False, height=False)
r = PhotoImage(file="E:\project\IMAGE BG\ROSE.png")
f = PhotoImage(file="E:\project\BUTTON\FFF.png")
ff = PhotoImage(file="E:\project\BUTTON\FFF2.png")
fff = PhotoImage(file="E:\project\BUTTON\FFF3.png")
bg_color=tk.Label(cartfram,image=r)
bg_color.place(x=0,y=0,width=1019,height=725)

c = PhotoImage(file="E:\project\IMAGE BG\CLASSY.png")

namestore=Label(cartfram,image=c, borderwidth="3px",cursor="heart", justify="center", relief="sunken")
namestore.place(x=100,y=7,width=498,height=66)

validate_func = cartfram.register(checkint)
quantity=tk.Entry(cartfram,validate='key',validatecommand=(validate_func, "%P"),bg="#000000", borderwidth="1px", cursor="heart", font=("Times", 10), fg="#ffffff", justify="center", relief="sunken")
quantity.place(x=20, y=670, width=99, height=40)

delete_button = tk.Button(cartfram, bg="#F9DEC9", cursor="heart", image=ff, font=("Times", 17), fg="#000000", justify="center", text="DELETE", borderwidth="3px", command=delete)
delete_button.place(x=220, y=670, width=80, height=40)


edit_button = tk.Button(cartfram, bg="#F9DEC9", cursor="heart", image=fff,font=("Times", 17), fg="#000000", justify="center", text="EDIT", borderwidth="3px", command=edit)
edit_button.place(x=130, y=670, width=80, height=40)


products_listbox = tk.Listbox(cartfram, bg="#ffffff", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
products_listbox.place(x=20, y=80, width=600, height=579)
price_listbox= tk.Listbox(cartfram, bg="#ffffff", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
price_listbox.place(x=620, y=80, width=280, height=579)
q_listbox = tk.Listbox(cartfram, bg="#ffffff", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
q_listbox.place(x=900, y=80, width=81, height=579)

GButton_724 = tk.Button(cartfram, text="PAY", bg="#f0f0f0", font=tkFont.Font(family='Times', size=10), fg="#000000", justify="center")
GButton_724.place(x=850, y=670, width=140, height=40)

end = tk.Button(cartfram, bg="#ff0000", font=("Times", 20), justify="center", text="X", borderwidth="3px", command=back)
end.place(x=940, y=17, width=50, height=50)

show()
cartfram.mainloop()
