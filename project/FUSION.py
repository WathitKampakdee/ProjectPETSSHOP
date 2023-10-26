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
def checkint(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False  
def shop(): 
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
        bgorder.destroy() 
        namestore.destroy() 
        cart.destroy() 
        end_order.destroy() 
        gg.destroy() 
        canvas.destroy() 
        product.destroy() 

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    #-----------------------------------------------------------------------------------------------------
    def cc():    
        tempidproduct=[] 
        totalprice=[]      
        def edit():
            selected_product = products_listbox.curselection()
            if selected_product:
                a = selected_product[0]
                idedit = tempidproduct[a]
                name = quantity.get()
                cursor.execute('''UPDATE myorder SET quantity=? WHERE id =? ''',(name,idedit))
                quantity.delete(0, tk.END)
                conn.commit()
                show()

        def delete():
            selected_product = products_listbox.curselection()
            if selected_product:
                a = selected_product[0]
                product_id = tempidproduct[a]
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
            tempidproduct.clear()
            totalprice.clear()
            for x in result:
                products_listbox.delete(0, tk.END)
                c=conn.cursor()   
                c.execute('''SELECT * FROM myorder''')
                result=c.fetchall()
                i=1
            for x in result:
                products_listbox.insert(x[0]," Product No:  {}    {}   ".format(i,x[1]))
                tempidproduct.append(x[0])
                i+=1  
            for y in result:
                q_listbox.insert(y[3]," ▶  {}  ".format(y[3]))
            for y in result:
                price_listbox.insert(y[3],"        {}   THB".format(y[2]))   
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
            bgcart.destroy()

        bgcart = Label(root, bg="#c71585",image=imagebg,cursor="heart")
        bgcart.place(x=0, y=0, width=1019, height=730)

        namestore1=Label(root,image=c, borderwidth="3px",cursor="heart", justify="center", relief="sunken")
        namestore1.place(x=100,y=7,width=498,height=66)

        validate_func = root.register(checkint)
        quantity=tk.Entry(root,validate='key',validatecommand=(validate_func, "%P"),bg="#000000", borderwidth="1px", cursor="heart", font=("Times", 10), fg="#ffffff", justify="center", relief="sunken")
        quantity.place(x=20, y=670, width=99, height=40)

        delete_button = tk.Button(root, bg="#F9DEC9", cursor="heart", image=deletebutton, font=("Times", 17), fg="#000000", justify="center", text="DELETE", borderwidth="3px", command=delete)
        delete_button.place(x=220, y=670, width=80, height=40)


        edit_button = tk.Button(root, bg="#F9DEC9", cursor="heart", image=fff,font=("Times", 17), fg="#000000", justify="center", text="EDIT", borderwidth="3px", command=edit)
        edit_button.place(x=130, y=670, width=80, height=40)

        products_listbox = tk.Listbox(root, bg="#f7e2d0", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
        products_listbox.place(x=20, y=80, width=600, height=579)
        
        price_listbox= tk.Listbox(root, bg="#f7e2d0", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
        price_listbox.place(x=620, y=80, width=280, height=579)
        
        q_listbox = tk.Listbox(root, bg="#f7e2d0", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
        q_listbox.place(x=900, y=80, width=81, height=579)

        pay = tk.Button(root, text="PAY", bg="#f0f0f0", font=tkFont.Font(family='Times', sitempidproducte=10), fg="#000000", justify="center")
        pay.place(x=850, y=670, width=140, height=40)

        end = tk.Button(root, bg="#ff0000", font=("Times", 20), justify="center", text="X", borderwidth="3px", command=back1)
        end.place(x=940, y=17, width=50, height=50)
        show()
    #-----------------------------------------------------------------------------------------------------
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

def admin():
    tempidproduct=[]       
    def edit():
        selected_product = products_listbox.curselection()
        if selected_product:
            a = selected_product[0]
            idedit = tempidproduct[a]
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
            product_id = tempidproduct[a]
            cursor.execute("DELETE FROM mystore WHERE id=?", (product_id,))
            conn.commit()
            show()       

    def show():
        products_listbox.delete(0, tk.END)
        c = conn.cursor()
        c.execute('''SELECT * FROM mystore''')
        result = c.fetchall()
        i = 1
        tempidproduct.clear()

        for x in result:
            products_listbox.delete(0, tk.END)
            c=conn.cursor()   
            c.execute('''SELECT * FROM mystore''')
            result=c.fetchall()
            i=1
            tempidproduct.clear()
            for x in result:
                products_listbox.insert(x[0]," Product No:  {}    {}    price:  {}  quantity:  {}  ".format(i,x[1],x[2],x[3]))
                tempidproduct.append(x[0])
                i+=1         

        
    def back():
        bg_color.destroy() 
        name_entry.destroy() 
        price_entry.destroy() 
        quantity_entry.destroy() 
        add_button.destroy() 
        delete_button.destroy() 
        edit_button.destroy() 
        labelnameadmin.destroy() 
        labelpriceadmin.destroy() 
        labelquantityadmin.destroy()
        products_listbox.destroy()
        endadmin.destroy() 

            
    bg_color=tk.Label(root,image=imagebg)
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

    delete_button = tk.Button(root, bg="#F9DEC9", cursor="heart", image=deletebutton, font=("Times", 17), fg="#000000", justify="center", text="DELETE", borderwidth="3px", command=delete)
    delete_button.place(x=660, y=160, width=328, height=64)

    edit_button = tk.Button(root, bg="#F9DEC9", cursor="heart", image=fff,font=("Times", 17), fg="#000000", justify="center", text="EDIT", borderwidth="3px", command=edit)
    edit_button.place(x=660, y=249, width=328, height=64)

    labelnameadmin = tk.Label(root, bg="#000000", font=("Times", 13), fg="#ffffff",cursor="heart", justify="center",borderwidth="1px", text="PRODUCT NAME", relief="sunken")
    labelnameadmin.place(x=170, y=40, width=140, height=30)

    labelpriceadmin = tk.Label(root, bg="#000000", font=("Times", 13), fg="#ffffff",cursor="heart", justify="center",borderwidth="1px", text="PRODUCT PRICE", relief="sunken")
    labelpriceadmin.place(x=170, y=140, width=140, height=30)

    labelquantityadmin = tk.Label(root, bg="#000000", font=("Times", 13), fg="#ffffff",cursor="heart", justify="center",borderwidth="1px", text="QUANTITY", relief="sunken")
    labelquantityadmin.place(x=170, y=240, width=140, height=30)

    products_listbox = tk.Listbox(root, bg="#ffffff", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
    products_listbox.place(x=30, y=350, width=959, height=353)
    endadmin = tk.Button(root, bg="#ff0000", font=("Times", 20), justify="center", text="X", borderwidth="3px", command=back)
    endadmin.place(x=940, y=17, width=40, height=40)
    show()
def closeprogram():
    root.withdraw()
root = tk.Tk()
root.title("CLASSY STORE")
width=1019
height=730
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
imagebg = PhotoImage(file="E:\project\IMAGE BG\ROSE.png")
m = PhotoImage(file="E:\project\IMAGE BG\mm.png")
i = PhotoImage(file="E:\project\IMAGE BG\CCC.png")
c = PhotoImage(file="E:\project\IMAGE BG\CLASSY.png")
deletebutton = PhotoImage(file="E:\project\BUTTON\FFF2.png")
fff = PhotoImage(file="E:\project\BUTTON\FFF3.png")
f = PhotoImage(file="E:\project\BUTTON\FFF.png")
bghomepage = PhotoImage(file="E:\project\GFGUI\homepage\homepage.png")
bgshop = PhotoImage(file="E:/project/GFGUI/homepage/buynow.png")
bgadmin = PhotoImage(file="E:/project/GFGUI/homepage/admin.png")
bgclose = PhotoImage(file="E:\project\GFGUI\homepage\close.png")



bgmain = tk.Label(root, bg="#ff99cc",image=imagebg).place(x=0, y=0, width=1017, height=730)
buttonshop = tk.Button(root, text="START SHOPING", bg="#a020f0", fg="#ffffff", cursor="heart", font=("Times", 14), justify="center",image=bgshop, command=shop).place(x=390, y=390, width=256, height=67)
buttonadmin = tk.Button(root, text="ADMIN", bg="#1e90ff", fg="#ffffff",image=bgadmin, cursor="heart", font=("Times", 14), justify="center", borderwidth="4px", relief="groove",command=admin).place(x=390, y=490, width=256, height=67)
buttonclose = tk.Button(root, text="CLOSE", bg="#cc0000", fg="#ffffff",image=bgclose, cursor="heart", font=("Times", 14), justify="center", borderwidth="4px", relief="groove",command=closeprogram).place(x=390, y=600, width=256, height=67)
root.mainloop()

