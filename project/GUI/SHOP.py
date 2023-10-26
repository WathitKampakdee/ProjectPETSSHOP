import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import random
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import io


conn = sqlite3.connect(r"E:\project\databeta.db")
cursor = conn.cursor()

def display_show_product():
    
    cursor.execute("SELECT * FROM mystore")
    pictures = cursor.fetchall()
    
    def addtocart(item):
        def add():
            c = conn.cursor()
            c.execute("INSERT INTO myorder (name, price, quantity, picture) VALUES (?, ?, ?, ?)", (item[1], item[2], 1, item[4]))
            conn.commit()
        return add

    for i, x in enumerate(pictures):
        image = Image.open(BytesIO(x[4]))
        target_width, target_height = 128, 128
        image = image.resize((target_width, target_height))
        image = ImageTk.PhotoImage(image)

        label1 = Button(product, image=image, text=" {}  $ {} ".format(x[1], x[2]), compound="top", command=addtocart(x), bg= "#000000", fg="#ffffff")
        label1.image = image
        label1.grid(row=i // 6, column=i % 6, padx=10, pady=10)
    
def back():
    root.destroy() 
def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

#-----------------------------------------------------------------------------------------------------
def cc():
    namestore.destroy()
    cart.destroy()
    end_order.destroy()

    
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
            name = quantity.get()
            cursor.execute('''UPDATE myorder SET quantity=? WHERE id =? ''',(name,idedit))
            quantity.delete(0, tk.END)
            conn.commit()
            show()


    def delete():
        selected_product = products_listbox.curselection()
        if selected_product:
            a = selected_product[0]
            product_id = z[a]
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
        z.clear()
        for x in result:
            products_listbox.insert(x[0]," Product No:  {}    {}   ".format(i,x[1]))
            z.append(x[0])
            i+=1  
        for x in result:
            price_listbox.insert(x[3],"        {}   THB".format(x[2]))
        for x in result:
            q_listbox.insert(x[3]," ▶  {}  ".format(x[3]))
                

        
    def back1(): 
        namestore1.destroy()     
        quantity.destroy()
        delete_button.destroy()
        edit_button.destroy()
        products_listbox.destroy()
        price_listbox.destroy()
        q_listbox.destroy()
        pay.destroy()
        end.destroy()


        namestore=Label(root,image=c)
        namestore.place(x=250,y=25,width=498,height=66)

        cart1 = Button(root, bg="#ffffff", cursor="heart",image=i, fg="#000000", justify="center",  relief="groove", borderwidth="1px",command=cc)
        cart1.place(x=830,y=30, width=65, height=55)

        end_order = Button(root, bg="#ff0000", cursor="heart", font=("Times", 20), justify="center", text="X", borderwidth="2px",command=back)
        end_order.place(x=930, y=30, width=51, height=51)
        display_show_product()

    


    namestore1=Label(root,image=c, borderwidth="3px",cursor="heart", justify="center", relief="sunken")
    namestore1.place(x=100,y=7,width=498,height=66)

    validate_func = root.register(checkint)
    quantity=tk.Entry(root,validate='key',validatecommand=(validate_func, "%P"),bg="#000000", borderwidth="1px", cursor="heart", font=("Times", 10), fg="#ffffff", justify="center", relief="sunken")
    quantity.place(x=20, y=670, width=99, height=40)

    delete_button = tk.Button(root, bg="#F9DEC9", cursor="heart", image=ff, font=("Times", 17), fg="#000000", justify="center", text="DELETE", borderwidth="3px", command=delete)
    delete_button.place(x=220, y=670, width=80, height=40)


    edit_button = tk.Button(root, bg="#F9DEC9", cursor="heart", image=fff,font=("Times", 17), fg="#000000", justify="center", text="EDIT", borderwidth="3px", command=edit)
    edit_button.place(x=130, y=670, width=80, height=40)

    products_listbox = tk.Listbox(root, bg="#f7e2d0", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
    products_listbox.place(x=20, y=80, width=600, height=579)
    
    price_listbox= tk.Listbox(root, bg="#f7e2d0", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
    price_listbox.place(x=620, y=80, width=280, height=579)
    
    q_listbox = tk.Listbox(root, bg="#f7e2d0", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
    q_listbox.place(x=900, y=80, width=81, height=579)

    pay = tk.Button(root, text="PAY", bg="#f0f0f0", font=tkFont.Font(family='Times', size=10), fg="#000000", justify="center")
    pay.place(x=850, y=670, width=140, height=40)

    end = tk.Button(root, bg="#ff0000", font=("Times", 20), justify="center", text="X", borderwidth="3px", command=back1)
    end.place(x=940, y=17, width=50, height=50)

    show()

#-----------------------------------------------------------------------------------------------------


root = Tk()
root.title("CLASSY SHOP")
width1 = 1019
height1 = 730
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width1, height1, (sw - width1) / 2, (sh - height1) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

imagebg = PhotoImage(file="E:\project\IMAGE BG\ROSE.png")
m = PhotoImage(file="E:\project\IMAGE BG\mm.png")
i = PhotoImage(file="E:\project\IMAGE BG\CCC.png")
c = PhotoImage(file="E:\project\IMAGE BG\CLASSY.png")
ff = PhotoImage(file="E:\project\BUTTON\FFF2.png")
fff = PhotoImage(file="E:\project\BUTTON\FFF3.png")


bgorder = Label(root, bg="#c71585",image=imagebg,cursor="heart")
bgorder.place(x=0, y=0, width=1019, height=730)

namestore=Label(root,image=c)
namestore.place(x=250,y=25,width=498,height=66)

cart = Button(root, bg="#ffffff", cursor="heart",image=i, fg="#000000", justify="center",  relief="groove", borderwidth="1px",command=cc)
cart.place(x=830,y=30, width=65, height=55)

end_order = Button(root, bg="#ff0000", cursor="heart", font=("Times", 20), justify="center", text="X", borderwidth="2px",command=back)
end_order.place(x=930, y=30, width=51, height=51)
gg = Label(root, bg="#ffffff",image=m)
gg.place(x=30, y=100, width=938, height=530)

canvas = Canvas(root, bg="#f7e2d0")
canvas.place(x=30, y=100, width=938, height=530)
product = Frame(canvas, bg="#f7e2d0")
canvas.create_window((0, 0), window=product, anchor='nw')
root.bind("<MouseWheel>", on_mousewheel)

display_show_product()

root.mainloop()


