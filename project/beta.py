import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import sqlite3
from tkinter import filedialog
import io
from PIL import Image, ImageTk
#วันที่ ตกแแต่ง รูปภาพ ป้ายtitle ผู้พัฒนา  
conn=sqlite3.connect(r"E:\project\databeta.db")
cursor = conn.cursor()


def showbill():
    def moneybill():      
        bill.delete(0, tk.END)
        c=conn.cursor()   
        c.execute('''SELECT * FROM myorder''')
        result=c.fetchall()
        totalprice=0  
        i=1
        for y in result:
            bill.insert(tk.END,"Product No:  {}   {}   ${}".format(i,y[1],y[2]))
            totalprice += y[2]
            tatolbill.config(text=f"Total Price: ${totalprice:.2f}")
            i+=1
    def back():
        root.destroy() 
               
    root = tk.Tk()
    root.title("CLASSY BILL")
    width=1019
    height=730
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    bgg = tk.Label(root, bg="#c71585", cursor="heart")
    bgg.place(x=0, y=0, width=1017, height=727)

    bgbill=tk.Label(root)
    bgbill["bg"] = "#e87eab"
    bgbill["cursor"] = "heart"
    bgbill.place(x=320,y=20,width=391,height=682)
    bill = tk.Listbox(root, bg="#fef0b7", borderwidth="1px", cursor="heart", font=("Times", 15), fg="#000000")
    bill.place(x=340, y=120, width=349, height=565)
    namebill = tk.Label(root, bg="#c71585", cursor="heart", font=("Times", 12), fg="#ffffff", justify="center", text="CLASSY STORE BILL", relief="sunken")
    namebill.place(x=440, y=60, width=160, height=34)
    font1 = tk.Label(root, bg="#c71585", cursor="heart", font=("Times", 60), fg="#ffffff", justify="center", text="THANK")
    font1.place(x=30, y=300, width=280, height=65)
    font2 = tk.Label(root, bg="#c71585", cursor="heart", font=("Times", 60), fg="#ffffff", justify="center", text="YOU")
    font2.place(x=740, y=300, width=260, height=65)
    tatolbill = tk.Label(root, bg="#fef0b7", cursor="heart", font=("Times", 18), fg="#000000", justify="center", text="TOTAL")
    tatolbill.place(x=435, y=650, width=250, height=35)
    endpay = tk.Button(root, bg="#ff0000", font=("Times", 10), justify="center", text="X", command=back)
    endpay.place(x=930, y=30, width=30, height=30)
    moneybill()
    root.mainloop()
def checkint(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False  
def admin():
    def admin():
        z=[]       
        def edit():
            selected_product = products_listbox.curselection()
            if selected_product:
                a = selected_product[0]
                idedit = z[a]
                name = name_entry.get()
                price = price_entry.get()
                cursor.execute('''UPDATE mystore SET name =?,price =? WHERE id =? ''',(name, price,idedit))
                name_entry.delete(0, tk.END)
                price_entry.delete(0, tk.END)
                conn.commit()
                show()
        def add():
            name = name_entry.get()
            price =price_entry.get()  
            if name and price:
                cursor.execute("INSERT INTO mystore (name, price) VALUES (?, ?)", (name, price))
                conn.commit()
                name_entry.delete(0, tk.END)
                price_entry.delete(0, tk.END)
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
            c=conn.cursor()   
            c.execute('''SELECT * FROM mystore''')
            result=c.fetchall()
            i=1
            z.clear()
            for x in result:
                products_listbox.insert(x[0]," Product No:  {}    {}    price: {}".format(i,x[1],x[2]))
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
        bg_color=tk.Label(root,bg= "#c71585")
        bg_color.place(x=0,y=0,width=1017,height=725)
        name_entry = tk.Entry(root, bg="#ff99cc", borderwidth="1px", cursor="heart", font=("Times", 10), fg="#333333", justify="center", relief="sunken")
        name_entry.place(x=30, y=70, width=527, height=103)
        validate_func = root.register(checkint)
        price_entry=tk.Entry(root,validate='key',validatecommand=(validate_func, "%P"),bg="#ff99cc", borderwidth="1px", cursor="heart", font=("Times", 10), fg="#333333", justify="center", relief="sunken")
        price_entry.place(x=30,y=210,width=527,height=103)
        add_button = tk.Button(root, bg="#ffcccc", cursor="heart", font=("Times", 17), fg="#000000", justify="center", text="ADD", relief="groove", borderwidth="3px", command=add)
        add_button.place(x=660, y=70, width=328, height=64)
        delete_button = tk.Button(root, bg="#ffcccc", cursor="heart", font=("Times", 17), fg="#000000", justify="center", text="DELETE", relief="groove", borderwidth="3px", command=delete)
        delete_button.place(x=660, y=160, width=328, height=64)
        edit_button = tk.Button(root, bg="#ffcccc", cursor="heart", font=("Times", 17), fg="#000000", justify="center", text="EDIT", relief="groove", borderwidth="3px", command=edit)
        edit_button.place(x=660, y=249, width=328, height=64)
        name_label = tk.Label(root, bg="#c71585", font=("Times", 13), fg="#ffffff", justify="center",borderwidth="1px", text="PRODUCT NAME", relief="sunken")
        name_label.place(x=30, y=40, width=140, height=30)
        price_label = tk.Label(root, bg="#c71585", font=("Times", 13), fg="#ffffff", justify="center",borderwidth="1px", text="PRODUCT PRICE", relief="sunken")
        price_label.place(x=30, y=180, width=140, height=30)
        products_listbox = tk.Listbox(root, bg="#ffccff", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
        products_listbox.place(x=30, y=350, width=959, height=353)
        end = tk.Button(root, bg="#ff0000", font=("Times", 20), justify="center", text="X", borderwidth="3px", command=back)
        end.place(x=940, y=17, width=40, height=40)

        show()
        root.mainloop()
    admin()

def shop():
    def shop():
        z=[]
        t=[]
        def add():
            selected_product = products_listbox.curselection()
            if selected_product:
                a = selected_product[0]
                id = z[a]
                c=conn.cursor() 
                c.execute("SELECT * FROM mystore WHERE id=?",(id,))
                result=c.fetchall()
                for x in result:
                    cursor.execute("INSERT INTO myorder (name, price) VALUES (?,?)", (x[1], x[2]))
                conn.commit()
                show()
                show1()
                show2()
                showpriceproduct()    
        def delete():
            selected_product = order_listbox.curselection()
            if selected_product:
                a = selected_product[0]
                product_id = t[a]
                cursor.execute("DELETE FROM myorder WHERE id=?", (product_id,))
                conn.commit()
                show1()
                show2()
                showpriceproduct()
        def show():      
            products_listbox.delete(0, tk.END)
            c=conn.cursor()   
            c.execute('''SELECT * FROM mystore''')
            result=c.fetchall()
            i=1
            z.clear()
            for x in result:
                products_listbox.insert(tk.END," Product No:  {}  {}".format(i,x[1]))
                z.append(x[0])
                i+=1       
        def showpriceproduct():      
            price_products_listbox.delete(0, tk.END)
            c=conn.cursor()   
            c.execute('''SELECT * FROM mystore''')
            result=c.fetchall()
            for y in result:
                price_products_listbox.insert(tk.END," {}".format(y[2]))
        def show1():      
            order_listbox.delete(0, tk.END)
            c=conn.cursor()   
            c.execute('''SELECT * FROM myorder''')
            result=c.fetchall()
            totalprice=0  
            i=1
            t.clear()
            for y in result:
                order_listbox.insert(y[0]," Product No:  {}   {}".format(i,y[1]))
                totalprice += y[2]
                total_label.config(text=f"Total Price: ${totalprice:.2f}")
                t.append(y[0])
                i+=1
        def show2():      
            price_order_listbox.delete(0, tk.END)
            c=conn.cursor()   
            c.execute('''SELECT * FROM myorder''')
            result=c.fetchall()
            for y in result:
                price_order_listbox.insert(tk.END," {}".format(y[2]))       
        def back():
            root.destroy()
        def pay():
            showbill()
            
        root = tk.Tk()
        root.title("CLASSY SHOP")
        width=1019
        height=730
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
                
        bgorder = tk.Label(root, bg="#c71585")
        bgorder.place(x=0,y=0,width=1020,height=730)
        addorder = tk.Button(root, bg="#cc99ff",cursor="heart", font=("Times", 15), fg="#000000", justify="center", text="ADD PRODUCT", relief="groove", borderwidth="3px", command=add)
        addorder.place(x=30, y=30, width=279, height=51)
        delete_order = tk.Button(root, bg="#ccccff",cursor="heart", font=("Times", 15), fg="#000000", justify="center", text="DELETE PRODUCT", relief="groove", borderwidth="3px", command=delete)
        delete_order.place(x=335, y=30, width=279, height=51)
        pay_money = tk.Button(root, bg="#ccffff",cursor="heart", font=("Times", 15), fg="#000000", justify="center", text="PAY", relief="groove", borderwidth="3px", command=pay)
        pay_money.place(x=640, y=30, width=279, height=51)
        products_listbox = tk.Listbox(root, bg="#ffcccc",cursor="heart", borderwidth="4px", font=("Times", 15), fg="#333333")
        products_listbox.place(x=30, y=100, width=720, height=291)
        order_listbox = tk.Listbox(root, bg="#ffcccc",cursor="heart", borderwidth="4px", font=("Times", 15), fg="#333333")
        order_listbox.place(x=30, y=410, width=720, height=220)
        price_order_listbox = tk.Listbox(root, bg="#ffcccc",cursor="heart", borderwidth="4px", font=("Times", 15), fg="#333333")
        price_order_listbox.place(x=780, y=410, width=200, height=220)
        price_products_listbox = tk.Listbox(root, bg="#ffcccc",cursor="heart", borderwidth="4px", font=("Times", 15), fg="#333333")
        price_products_listbox.place(x=780, y=100, width=200, height=291)
        total_label = tk.Label(root, text="Total Price: $0.00", bg="#ffccff",cursor="heart", font=("Times", 12), fg="#1e90ff", justify="center")
        total_label.place(x=720, y=650, width=264, height=54)    
        endorder = tk.Button(root, bg="#ff0000",cursor="heart", font=("Times", 20), justify="center", text="X", borderwidth="2px", command=back)
        endorder.place(x=940, y=30, width=41, height=41)

        show()
        show1()
        show2()
        showpriceproduct()

        root.mainloop()
    shop()
def end():
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

bgmain = tk.Label(root, bg="#ff99cc").place(x=0, y=0, width=1017, height=730)
welcome = tk.Label(root, bg="#c71585", cursor="heart", font=("Times", 22), fg="#ffffff", justify="center", borderwidth="3px", text="WELCOME TO CLASSY STORE", relief="sunken").place(x=270, y=160, width=476, height=174)
buttonshop = tk.Button(root, text="START SHOPING", bg="#a020f0", fg="#ffffff", cursor="heart", font=("Times", 14), justify="center", borderwidth="4px", relief="groove", command=shop).place(x=390, y=390, width=234, height=67)
buttonshop = tk.Button(root, text="ADMIN", bg="#1e90ff", fg="#ffffff", cursor="heart", font=("Times", 14), justify="center", borderwidth="4px", relief="groove", command=admin).place(x=390, y=490, width=234, height=67)
buttonshop = tk.Button(root, text="CLOSE", bg="#cc0000", fg="#ffffff", cursor="heart", font=("Times", 14), justify="center", borderwidth="4px", relief="groove", command=end).place(x=390, y=600, width=234, height=67)
root.mainloop()
