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
z=[]       
def edit():
    selected_product = products_listbox.curselection()
    if selected_product:
        a = selected_product[0]
        idedit = z[a]
        name = name_entry.get()
        price = price_entry.get()
        quantity= quantity_entry.get()
        file_pic = filedialog.askopenfilename()
        if file_pic:
            with open(file_pic, 'rb') as file:
                picture = file.read()
        cursor.execute('''UPDATE mystore SET name =?,price =?,quantity=?,picture=? WHERE id =? ''',(name, price, quantity, picture,idedit))
        name_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        conn.commit()
        show()
def add():
    name = name_entry.get()
    price =price_entry.get()
    quantity= quantity_entry.get()

    file_pic = filedialog.askopenfilename()
    if file_pic:
        with open(file_pic, 'rb') as file:
            picture = file.read()
    if name and price and quantity and picture:
        cursor.execute("INSERT INTO mystore (name, price,quantity,picture) VALUES (?, ?, ?, ?)", (name, price, quantity, picture))
        conn.commit()
        name_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        show() 

def delete():
    selected_product = products_listbox.curselection()
    if selected_product:
        a = selected_product[0]
        product_id = z[a]
        cursor.execute("DELETE FROM mystore WHERE id=?", (product_id,))
        conn.commit()
        show()       

def show():
    products_listbox.delete(0, tk.END)
    c = conn.cursor()
    c.execute('''SELECT * FROM mystore''')
    result = c.fetchall()
    i = 1
    z.clear()

    for x in result:
        products_listbox.delete(0, tk.END)
        c=conn.cursor()   
        c.execute('''SELECT * FROM mystore''')
        result=c.fetchall()
        i=1
        z.clear()
        for x in result:
            products_listbox.insert(x[0]," Product No:  {}    {}    price:  {}  quantity:  {}  ".format(i,x[1],x[2],x[3]))
            z.append(x[0])
            i+=1         

      
def back():
    root.destroy()       
        
root = tk.Tk()
root.title("MANU_ADMIN")
width=1019
height=730
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
r = PhotoImage(file="E:\project\IMAGE BG\ROSE.png")
f = PhotoImage(file="E:\project\BUTTON\FFF.png")
ff = PhotoImage(file="E:\project\BUTTON\FFF2.png")
fff = PhotoImage(file="E:\project\BUTTON\FFF3.png")
bg_color=tk.Label(root,image=r)
bg_color.place(x=0,y=0,width=1017,height=725)
name_entry = tk.Entry(root, bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 10), fg="#000000", justify="center", relief="sunken")
name_entry.place(x=30, y=80, width=460, height=50)

validate_func = root.register(checkint)
price_entry=tk.Entry(root,validate='key',validatecommand=(validate_func, "%P"),bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 10), fg="#000000", justify="center", relief="sunken")
price_entry.place(x=30,y=180,width=460,height=50)
quantity_entry=tk.Entry(root,validate='key',validatecommand=(validate_func, "%P"),bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 10), fg="#000000", justify="center", relief="sunken")
quantity_entry.place(x=30,y=280,width=460,height=50)

add_button = tk.Button(root, bg="#F9DEC9", cursor="heart", image=f, font=("Times", 17), fg="#000000", justify="center", text="ADD",  borderwidth="3px", command=add)
add_button.place(x=660, y=70, width=328, height=64)

delete_button = tk.Button(root, bg="#F9DEC9", cursor="heart", image=ff, font=("Times", 17), fg="#000000", justify="center", text="DELETE", borderwidth="3px", command=delete)
delete_button.place(x=660, y=160, width=328, height=64)

edit_button = tk.Button(root, bg="#F9DEC9", cursor="heart", image=fff,font=("Times", 17), fg="#000000", justify="center", text="EDIT", borderwidth="3px", command=edit)
edit_button.place(x=660, y=249, width=328, height=64)

#addpic_button = tk.Button(root, bg="#ffcccc", cursor="heart", font=("Times", 10), fg="#000000", justify="center", text="PICTURE", relief="groove", borderwidth="3px")
#addpic_button.place(x=30, y=320, width=100, height=20)

name_label = tk.Label(root, bg="#000000", font=("Times", 13), fg="#ffffff",cursor="heart", justify="center",borderwidth="1px", text="PRODUCT NAME", relief="sunken")
name_label.place(x=170, y=40, width=140, height=30)

price_label = tk.Label(root, bg="#000000", font=("Times", 13), fg="#ffffff",cursor="heart", justify="center",borderwidth="1px", text="PRODUCT PRICE", relief="sunken")
price_label.place(x=170, y=140, width=140, height=30)

price_label = tk.Label(root, bg="#000000", font=("Times", 13), fg="#ffffff",cursor="heart", justify="center",borderwidth="1px", text="QUANTITY", relief="sunken")
price_label.place(x=170, y=240, width=140, height=30)

products_listbox = tk.Listbox(root, bg="#ffffff", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
products_listbox.place(x=30, y=350, width=959, height=353)

end = tk.Button(root, bg="#ff0000", font=("Times", 20), justify="center", text="X", borderwidth="3px", command=back)
end.place(x=940, y=17, width=40, height=40)
show()
root.mainloop()