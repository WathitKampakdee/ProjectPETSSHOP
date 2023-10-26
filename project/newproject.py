
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from datetime import datetime
from tkinter import messagebox
import hashlib
from fpdf import FPDF
import subprocess
#import tkinter as toplevel
#import random
conn = sqlite3.connect(r"E:\project\databeta.db")
cursor = conn.cursor()
now = datetime.today()
def logstore():
    conn = sqlite3.connect(r"E:\project\databeta.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM history')
    data = cursor.fetchall()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    cell_widths = [10, 50, 50, 10, 10, 60]

    for row in data:
        for i, item in enumerate(row):
            pdf.cell(cell_widths[i], 10, str(item), 1)
        
        pdf.ln()

    file_path = 'datastore.pdf'
    pdf.output(file_path)

    conn.close()

    subprocess.Popen(['start', file_path], shell=True)

def checkstock():
    checkstock=[]
    checkstock.clear
    cursor.execute("SELECT id,quantity FROM mystore")
    check = cursor.fetchall() 
    
    for x in check:
        checkstock.append(x[0])
    #print(checkstock)
    c=0
    for y in check:
        if y[1] <=0 :
            print(checkstock[c])
            cursor.execute("DELETE FROM mystore WHERE id=?", (checkstock[c],))
            conn.commit()  
        c+=1

    
def checkint(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False  
def shop(): 
    checkstock()
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
            target_width, target_height = 197, 197
            image = image.resize((target_width, target_height))
            image = ImageTk.PhotoImage(image)

            label1 = Button(product, font=("Times", 14), image=image, text=" {}  ฿ {} ".format(x[1], x[2]), compound="top", command=addtocart(x), bg= "#cecece", fg="#000000")
            label1.image = image
            label1.grid(row=i // 5, column=i % 5, padx=17, pady=10)
    def backstore():
        bgorder.destroy()  
        cart.destroy() 
        end_order.destroy() 
        gg.destroy()  
        product.destroy() 
        productdisplay.destroy() 
    def on_mousewheel(event):
        productdisplay.yview_scroll(int(-1*(event.delta/120)), "units")
    #-----------------------------------------------------------------------------------------------------
    def opencart(): 
        tempidproduct=[]   
        def edit():
            selected_product = products_listbox.curselection()
            if selected_product:
                a = selected_product[0]
                idedit = tempidproduct[a]
                orderquantity = int(quantity.get())
                c = conn.cursor()
                c.execute('''SELECT * FROM myorder''')
                result = c.fetchall()
                stoploop = False
                for x in result:
                    c = conn.cursor()
                    c.execute("SELECT id,name,quantity  FROM mystore  WHERE name=?",(x[1],))
                    resultstock = c.fetchall()
                    for y in resultstock:
                        if stoploop==False:
                            if orderquantity>y[2] :
                                messagebox.showinfo(title="Not enough product", message="Enter the quantity of new products.") 
                                quantity.delete(0, tk.END)   
                                stoploop=True                    
                                break     
                            else:
                                cursor.execute('''UPDATE myorder SET quantity=? WHERE id =? ''',(orderquantity,idedit))
                                quantity.delete(0, tk.END)
                                conn.commit()
                                show()
                        elif stoploop==True:
                            break
        def delete():
            selected_product = products_listbox.curselection()
            if selected_product:
                a = selected_product[0]
                product_id = tempidproduct[a]
                cursor.execute("DELETE FROM myorder WHERE id=?", (product_id,))
                conn.commit()
                show()       
        def show():
            totalprice=0  
            tempidproduct.clear()
            products_listbox.delete(0, tk.END)
            price_listbox.delete(0, tk.END)
            q_listbox.delete(0, tk.END)
            c = conn.cursor()
            c.execute('''SELECT * FROM myorder''')
            result = c.fetchall()
            for x in result:
                c = conn.cursor()
                c.execute("SELECT id,name,quantity  FROM mystore  WHERE name=?",(x[1],))
                resultstock = c.fetchall()
                for y in resultstock:
                    products_listbox.insert(x[0]," ▶                 {}   ".format(x[1]))
                    tempidproduct.append(x[0])
                    totalprice+= x[2]*x[3]
                    totalpricelabel.config(text=f"Total Price: ฿{totalprice:.2f}")
                    q_listbox.insert(x[0]," {} * {} = {}  THB".format(x[2],x[3],x[2]*x[3]))   
                    price_listbox.insert(x[0]," ▶In Stock  {}  ▶In Cart  {} ".format(y[2]-x[3],x[3]))
        def backcart():      
            quantity.destroy()
            delete_button.destroy()
            edit_button.destroy()
            products_listbox.destroy()
            price_listbox.destroy()
            q_listbox.destroy()
            pay.destroy()
            end.destroy()
            bgcart.destroy()
            totalpricelabel.destroy()
#----------------------------------------bill--------------------------------------------------------------
        def membercheck():
            choice = messagebox.askquestion("Member", "คุณเป็นสมาชิกมั้ย?")   
            #print(choice) 
            if choice == 'yes':
                loginmember()
            if choice== 'no':
                bill() 
        def loginmember():
            def hash_password(passwordmem):
                return hashlib.sha256(passwordmem.encode()).hexdigest()

            def add_user(usernamemem, passwordmem):
                hashed_password = hash_password(passwordmem)
                cursor.execute('INSERT INTO member (username, password, level, passwordnothast) VALUES (?,?,?,?)', (usernamemem, hashed_password,0, passwordmem))
                conn.commit()

            def add_user1():
                usernamemem = username_entrymember.get()
                passwordmem = password_entrymember.get()

                if usernamemem and passwordmem:
                    add_user(usernamemem, passwordmem)
                    messagebox.showinfo('เพิ่มผู้ใช้', 'เพิ่มผู้ใช้เรียบร้อยแล้ว!')
                else:
                    messagebox.showerror('ข้อผิดพลาด', 'โปรดป้อนชื่อผู้ใช้และรหัสผ่านทั้งคู่.')
                username_entrymember.delete(0, tk.END)
                password_entrymember.delete(0, tk.END)

            def login():
                usernamemem = username_entrymember.get()
                passwordmem = password_entrymember.get()
                hashed_password = hash_password(passwordmem)
                cursor.execute('SELECT password FROM member WHERE username = ?', (usernamemem,))
                result = cursor.fetchone()
                if result and result[0] == hashed_password:
                    messagebox.showinfo('Login', '🔓Login successful!🔓')
                    billmem()
                    closing()
                else:
                    messagebox.showerror('Login', '🔒nvalid credentials.🔒')
                    username_entrymember.delete(0,tk.END)
                    password_entrymember.delete(0,tk.END)

            def closing():
                bgloginmember.destroy()
                username_entrymember.destroy()
                password_entrymember.destroy()
                add_user_buttonmember.destroy()
                login_buttonmember.destroy()
                exit_buttonmember.destroy()
            bgloginmember  = tk.Label(guimain, image=bghomepage, bg="#fea46b", cursor="heart")
            bgloginmember.place(x=0, y=0, width=1306, height=697)

            username_entrymember = tk.Entry(guimain, bg="#ffffff", borderwidth="3px", cursor="heart", font=tkFont.Font(family='Times', size=20), fg="#000000", justify="center")
            username_entrymember.place(x=465, y=250, width=368, height=60)

            password_entrymember = tk.Entry(guimain, bg="#ffffff", borderwidth="3px", cursor="heart", font=tkFont.Font(family='Times', size=20),show='🔒', fg="#000000", justify="center")
            password_entrymember.place(x=465, y=330, width=368, height=60)

            add_user_buttonmember = tk.Button(guimain, bg="#CECE5A", cursor="heart", font=tkFont.Font(family='Times', size=18), fg="#000000", justify="center", text="REGISTER", relief="sunken",command=add_user1)
            add_user_buttonmember.place(x=680, y=430, width=150, height=50)

            login_buttonmember = tk.Button(guimain, bg="#CECE5A", cursor="heart", font=tkFont.Font(family='Times', size=18), fg="#000000", justify="center", text="LOGIN", relief="sunken",command=login)
            login_buttonmember.place(x=465, y=430, width=150, height=50)

            exit_buttonmember = tk.Button(guimain, borderwidth="5px", cursor="heart", bg="#FF0000", fg="#000000", text="X",command=closing)
            exit_buttonmember.place(x=1250, y=10, width=44, height=40)


        def billmem():    
            def payment():
                def paytransfer():
                    c = conn.cursor()
                    c.execute('''SELECT * FROM myorder''')
                    result = c.fetchall()
                    date=now
                    category="sales,transfer payment"
                    for x in result:
                        c.execute("SELECT id,name,quantity  FROM mystore  WHERE name=?",(x[1],))
                        resultstock = c.fetchall()
                        for   x in result:
                            for y in resultstock:
                                cursor.execute('''UPDATE mystore SET quantity=? WHERE id =? ''',(y[2]-x[3],y[0]))
                                conn.commit()
                        namehistory,pricehistory,quantity=x[1],x[2],x[3]
                        print(category,"  /  ",namehistory,"  /  ",pricehistory,"  /  ",quantity,"  /  ",date)
                        if category and namehistory and pricehistory and quantity and date :
                            cursor.execute("INSERT INTO history (category,name,price,quantity,date) VALUES (?, ?, ?, ?, ?)", (category,namehistory,pricehistory,quantity,date))
                            conn.commit()
                        cursor.execute("DELETE FROM myorder")
                        conn.commit()
                        backbill()
                        backcart()
                        backstore()
                sumpay=0
                c = conn.cursor()
                c.execute('''SELECT * FROM myorder''')
                result = c.fetchall()
                date=now
                category="sales,transfer payment"
                for s in  result:
                    sumpay+=s[2]*s[3]
                sumpay=sumpay/100*95
                def pay():
                    scan =sumpay
                    text = "https://promptpay.io/0995043944/" + str(scan) + ".png"
                    image_url = text

                    response = requests.get(image_url)

                    if response.status_code == 200:
                        image = Image.open(BytesIO(response.content))

                        if image.mode != 'L':
                            image = image.convert('L')

                        image = image.resize((200, 200))  
                        img_tk = ImageTk.PhotoImage(image)
                        

                        lebel_qr = Label(guimain, image=img_tk)
                        lebel_qr.image = img_tk 
                        lebel_qr.place(x=1000, y=300)
                        def unokpay():
                            lebel_qr.destroy()
                            ok.destroy()
                            unok.destroy() 
                        def okpay():
                            lebel_qr.destroy()
                            ok.destroy()
                            unok.destroy()
                            paytransfer()
                            
                        ok = Button(guimain, font=("Times", 14),text="Ok",command=okpay) 
                        ok.place(x=990, y=180  ,height=70,width=100)
                        unok = Button(guimain, font=("Times", 14),text="Cancel",command=unokpay) 
                        unok.place(x=1120, y=180 ,height=70,width=100)
                    else:
                        print("Failed to download the image. HTTP status code:", response.status_code)
                pay()
                
            def cash():
                c = conn.cursor()
                c.execute('''SELECT * FROM myorder''')
                result = c.fetchall()
                date=now
                category="sales,cash"
                
                for x in result:
                    c.execute("SELECT id,name,quantity  FROM mystore  WHERE name=?",(x[1],))
                    resultstock = c.fetchall()
                    for   x in result:
                        for y in resultstock:
                            cursor.execute('''UPDATE mystore SET quantity=? WHERE id =? ''',(y[2]-x[3],y[0]))
                            conn.commit()
                    namehistory,pricehistory,quantity=x[1],x[2],x[3]
                    if category and namehistory and pricehistory and quantity and date :
                        cursor.execute("INSERT INTO history (category,name,price,quantity,date) VALUES (?, ?, ?, ?, ?)", (category,namehistory,pricehistory,quantity,date))
                        conn.commit()
                    cursor.execute("DELETE FROM myorder")
                    conn.commit()
                    backbill()
                    backcart()
                    backstore()
            def transferpayment():
                    payment()
            def show():
                        totalprice=0  
                        products_listbox5.delete(0, tk.END)
                        products_listbox5.insert(0,(now))
                        c = conn.cursor()
                        c.execute('''SELECT * FROM myorder''')
                        result = c.fetchall()
                        for x in result:
                            products_listbox5.insert(x[0]," ▶   {}    {} * {} = {}  THB  ".format(x[1],x[2],x[3],x[2]*x[3]))
                            totalprice+= x[2]*x[3]
                        products_listbox5.insert(tk.END,"     ")
                        products_listbox5.insert(tk.END,"       Voucher  Voucher  Voucher  Voucher    ")
                        products_listbox5.insert(tk.END," ▶ Voucher for member 5%   {}  -5 % = {}  THB  ".format(totalprice,totalprice/100*95))
                        totalprice-=totalprice/100*5
                        totalbill.config(text=f"Total Price: ฿{totalprice:.2f}")   
            def backbill():
                bg_bill.destroy()
                transferpayment_button.destroy()
                cash_button.destroy()
                totalbill.destroy()
                products_listbox5.destroy()
                end.destroy()    
            bg_bill=tk.Label(guimain,image=bgbill)
            bg_bill.place(x=0,y=0,width=1306,height=697)

            cash_button = tk.Button(guimain, bg="#F9DEC9", cursor="heart", font=("Times", 17), fg="#000000", justify="center", text="cash", borderwidth="3px",command=cash)
            cash_button.place(x=583, y=620, width=80, height=40)

            transferpayment_button = tk.Button(guimain, bg="#F9DEC9", cursor="heart",font=("Times", 17), fg="#000000", justify="center", text="Transfer payment", borderwidth="3px",command=transferpayment)
            transferpayment_button.place(x=685, y=620, width=200, height=40)

            totalbill = Label(guimain, text="Total Price: $0.00", bg="#ffffff",cursor="heart", font=("Times", 12), fg="#000000", justify="center",borderwidth="3px")
            totalbill.place(x=685, y=570, width=200, height=40)

            products_listbox5 = tk.Listbox(guimain, bg="#ffffff", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
            products_listbox5.place(x=420, y=150, width=470, height=400)

            end = tk.Button(guimain, borderwidth="5px", cursor="heart", bg="#FF0000", fg="#000000", text="X",command=backbill)
            end.place(x=1250, y=10, width=44, height=40)
            show()

        def bill():    
            def payment():
                def paytransfer():
                    c = conn.cursor()
                    c.execute('''SELECT * FROM myorder''')
                    result = c.fetchall()
                    date=now
                    category="sales,transfer payment"
                    for x in result:
                        c.execute("SELECT id,name,quantity  FROM mystore  WHERE name=?",(x[1],))
                        resultstock = c.fetchall()
                        for   x in result:
                            for y in resultstock:
                                cursor.execute('''UPDATE mystore SET quantity=? WHERE id =? ''',(y[2]-x[3],y[0]))
                                conn.commit()
                        namehistory,pricehistory,quantity=x[1],x[2],x[3]
                        print(category,"  /  ",namehistory,"  /  ",pricehistory,"  /  ",quantity,"  /  ",date)
                        if category and namehistory and pricehistory and quantity and date :
                            cursor.execute("INSERT INTO history (category,name,price,quantity,date) VALUES (?, ?, ?, ?, ?)", (category,namehistory,pricehistory,quantity,date))
                            conn.commit()
                        cursor.execute("DELETE FROM myorder")
                        conn.commit()
                        backbill()
                        backcart()
                        backstore()
                sumpay=0
                c = conn.cursor()
                c.execute('''SELECT * FROM myorder''')
                result = c.fetchall()
                date=now
                category="sales,transfer payment"
                for s in  result:
                    sumpay+=s[2]*s[3]
                def pay():
                    scan =sumpay
                    text = "https://promptpay.io/0995043944/" + str(scan) + ".png"
                    image_url = text

                    response = requests.get(image_url)

                    if response.status_code == 200:
                        image = Image.open(BytesIO(response.content))

                        if image.mode != 'L':
                            image = image.convert('L')

                        image = image.resize((200, 200))  
                        img_tk = ImageTk.PhotoImage(image)
                        

                        lebel_qr = Label(guimain, image=img_tk)
                        lebel_qr.image = img_tk 
                        lebel_qr.place(x=1000, y=300)
                        def unokpay():
                            lebel_qr.destroy()
                            ok.destroy()
                            unok.destroy() 
                        def okpay():
                            lebel_qr.destroy()
                            ok.destroy()
                            unok.destroy()
                            paytransfer()
                            
                        ok = Button(guimain, font=("Times", 14),text="Ok",command=okpay) 
                        ok.place(x=990, y=180  ,height=70,width=100)
                        unok = Button(guimain, font=("Times", 14),text="Cancel",command=unokpay) 
                        unok.place(x=1120, y=180 ,height=70,width=100)
                    else:
                        print("Failed to download the image. HTTP status code:", response.status_code)
                pay()
            def cash():
                c = conn.cursor()
                c.execute('''SELECT * FROM myorder''')
                result = c.fetchall()
                date=now
                category="sales,cash"
                for x in result:
                    c.execute("SELECT id,name,quantity  FROM mystore  WHERE name=?",(x[1],))
                    resultstock = c.fetchall()
                    for   x in result:
                        for y in resultstock:
                            cursor.execute('''UPDATE mystore SET quantity=? WHERE id =? ''',(y[2]-x[3],y[0]))
                            conn.commit()
                    namehistory,pricehistory,quantity=x[1],x[2],x[3]
                    if category and namehistory and pricehistory and quantity and date :
                        cursor.execute("INSERT INTO history (category,name,price,quantity,date) VALUES (?, ?, ?, ?, ?)", (category,namehistory,pricehistory,quantity,date))
                        conn.commit()
                    cursor.execute("DELETE FROM myorder")
                    conn.commit()
                    backbill()
                    backcart()
                    backstore()
            def transferpayment():
                    payment()
            def show():
                        totalprice=0  
                        products_listbox5.delete(0, tk.END)
                        products_listbox5.insert(0,(now))
                        c = conn.cursor()
                        c.execute('''SELECT * FROM myorder''')
                        result = c.fetchall()
                        for x in result:
                            products_listbox5.insert(x[0]," ▶   {}    {} * {} = {}  THB  ".format(x[1],x[2],x[3],x[2]*x[3]))
                            totalprice+= x[2]*x[3]
                        totalbill.config(text=f"Total Price: ฿{totalprice:.2f}")   
            def backbill():
                bg_bill.destroy()
                transferpayment_button.destroy()
                cash_button.destroy()
                totalbill.destroy()
                products_listbox5.destroy()
                end.destroy()    
            bg_bill=tk.Label(guimain,image=bgbill)
            bg_bill.place(x=0,y=0,width=1306,height=697)

            cash_button = tk.Button(guimain, bg="#F9DEC9", cursor="heart", font=("Times", 17), fg="#000000", justify="center", text="cash", borderwidth="3px",command=cash)
            cash_button.place(x=583, y=620, width=80, height=40)

            transferpayment_button = tk.Button(guimain, bg="#F9DEC9", cursor="heart",font=("Times", 17), fg="#000000", justify="center", text="Transfer payment", borderwidth="3px",command=transferpayment)
            transferpayment_button.place(x=685, y=620, width=200, height=40)

            totalbill = Label(guimain, text="Total Price: $0.00", bg="#ffffff",cursor="heart", font=("Times", 12), fg="#000000", justify="center",borderwidth="3px")
            totalbill.place(x=685, y=570, width=200, height=40)

            products_listbox5 = tk.Listbox(guimain, bg="#ffffff", borderwidth="4px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
            products_listbox5.place(x=420, y=150, width=470, height=400)

            end = tk.Button(guimain, borderwidth="5px", cursor="heart", bg="#FF0000", fg="#000000", text="X",command=backbill)
            end.place(x=1250, y=10, width=44, height=40)
            show()

#----------------------------------------billmem--------------------------------------------------------------

        bgcart = Label(guimain, bg="#c71585",image=blackgcart,cursor="heart")
        bgcart.place(x=0, y=0, width=1306, height=697)

        validate_func = guimain.register(checkint)
        quantity=tk.Entry(guimain,validate='key',validatecommand=(validate_func, "%P"), bg="#ffffff", borderwidth="3px", cursor="heart", font=("Times", 10), fg="#000000", justify="center", relief="sunken")
        quantity.place(x=920, y=93, width=201, height=40)

        delete_button = tk.Button(guimain, cursor="heart", image=bgicondelete, command=delete)
        delete_button.place(x=1140, y=90, width=49, height=43)

        edit_button = tk.Button(guimain,bg="#ffffff", cursor="heart", image=bgiconedit, font=("Times", 14), fg="#000000", command=edit)
        edit_button.place(x=1205, y=90, width=49, height=43)

        products_listbox = tk.Listbox(guimain, bg="#7a7a7a", borderwidth="1px", cursor="heart", font=("Times", 20), fg="#333333", relief="sunken")
        products_listbox.place(x=50, y=201, width=590, height=420)
        
        price_listbox= tk.Listbox(guimain, bg="#7a7a7a", borderwidth="1px", cursor="heart", font=("Times", 20), fg="#333333", relief="sunken")
        price_listbox.place(x=640, y=201, width=340, height=420)
        
        q_listbox = tk.Listbox(guimain, bg="#7a7a7a", borderwidth="1px", cursor="heart", font=("Times", 20), fg="#333333", relief="sunken")
        q_listbox.place(x=980, y=201, width=275, height=420)

        pay = tk.Button(guimain, fg="#000000", justify="center",image=bgiconpay,command=membercheck)
        pay.place(x=1200, y=635, width=49, height=43)

        totalpricelabel = Label(guimain, text="Total Price: $0.00", bg="#ffffff",cursor="heart", font=("Times", 12), fg="#000000", justify="center",borderwidth="3px")
        totalpricelabel.place(x=990, y=635, width=191, height=43)

        end= tk.Button(guimain, borderwidth="5px", cursor="heart", bg="#FF0000", fg="#000000", text="X",command=backcart)
        end.place(x=1250, y=10, width=44, height=40)
        show()
    #-----------------------------------------------------------------------------------------------------
    bgorder = Label(guimain,image=bgbuynow,cursor="heart")
    bgorder.place(x=0, y=0, width=1306, height=697)
    cart = Button(guimain, cursor="heart",image=bgiconcart,command=opencart)
    cart.place(x=1200,y=85, width=49, height=43)
    end_order = tk.Button(guimain, borderwidth="5px", cursor="heart", bg="#FF0000", fg="#000000", text="X",command=backstore)
    end_order.place(x=1250, y=10, width=44, height=40)

    gg = Label(guimain)
    gg.place(x=50, y=145, width=1200, height=510)
    productdisplay = Canvas(guimain, bg="#7a7a7a")
    productdisplay.place(x=52, y=147, width=1195, height=510)
    product = Frame(productdisplay, bg="#7a7a7a")
    productdisplay.create_window((0, 0), window=product, anchor='nw')
    guimain.bind("<MouseWheel>", on_mousewheel)
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
            category="admin,editproduct"
            namehistory=name
            pricehistory=price
            quantityhistory=quantity
            date=now
            cursor.execute("INSERT INTO history (category,name,price,quantity,date) VALUES (?, ?, ?, ?, ?)", (category,namehistory,pricehistory,quantityhistory,date))
            conn.commit()
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
            category="admin,addproduct"
            namehistory=name
            pricehistory=price
            quantityhistory=quantity
            date=now
            cursor.execute("INSERT INTO history (category,name,price,quantity,date) VALUES (?, ?, ?, ?, ?)", (category,namehistory,pricehistory,quantityhistory,date))
            conn.commit()
            name_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)
            show()
    def delete():
        selected_product = products_listbox.curselection()
        if selected_product:
            a = selected_product[0]
            c = conn.cursor()
            c.execute("SELECT name,price,quantity FROM mystore WHERE id=?", (tempidproduct[a],))
            result=c.fetchall()
            for x in result:
                namehistory=x[0]
                pricehistory=x[1]
                quantityhistory=x[2]
            date=now
            category="admin,deleteproduct"
            cursor.execute("INSERT INTO history (category,name,price,quantity,date) VALUES (?, ?, ?, ?, ?)", (category,namehistory,pricehistory,quantityhistory,date))
            conn.commit()                
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
            adminprice_listbox.delete(0, tk.END)
            adminquantity_listbox.delete(0, tk.END)
            picture_listbox.delete(0, tk.END)
            c=conn.cursor()   
            c.execute('''SELECT * FROM mystore''')
            result=c.fetchall()
            tempidproduct.clear()
            for x in result:
                products_listbox.insert(x[0],"  {}    ".format(x[1]))
                adminprice_listbox.insert(x[0],"  {}  THB   ".format(x[2])) 
                adminquantity_listbox.insert(x[0],"  {}    ".format(x[3]))  
                picture_listbox.insert(x[0]," {}    ".format(x[4]))   
                tempidproduct.append(x[0])         
    def back():
        bg_color.destroy() 
        name_entry.destroy() 
        price_entry.destroy() 
        quantity_entry.destroy() 
        add_button.destroy() 
        delete_button.destroy() 
        edit_button.destroy() 
        products_listbox.destroy()
        adminprice_listbox.destroy()
        adminquantity_listbox.destroy()
        picture_listbox.destroy()
        endadmin.destroy() 
        log.destroy()
        label1.destroy()
        label2.destroy()
        label3.destroy()
    bg_color=tk.Label(guimain,image=bgadmin)
    bg_color.place(x=0,y=0,width=1306,height=697)
    name_entry = tk.Entry(guimain, bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 22), fg="#000000", justify="center", relief="sunken")
    name_entry.place(x=527,y=70,width=630,height=50)
    validate_func = guimain.register(checkint)
    price_entry=tk.Entry(guimain,validate='key',validatecommand=(validate_func, "%P"),bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 22), fg="#000000", justify="center", relief="sunken")
    price_entry.place(x=527,y=130,width=630,height=50)
    quantity_entry=tk.Entry(guimain,validate='key',validatecommand=(validate_func, "%P"),bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 22), fg="#000000", justify="center", relief="sunken")
    quantity_entry.place(x=527,y=195,width=630,height=50)

    add_button = tk.Button(guimain, cursor="heart", image=iconaddadmin, font=("Times", 17), fg="#000000", justify="center", text="ADD",  borderwidth="3px", command=add)
    add_button.place(x=1200, y=70, width=49, height=43)

    delete_button = tk.Button(guimain, cursor="heart", image=icondeleteadmin, font=("Times", 17), fg="#000000", justify="center", text="DELETE", borderwidth="3px", command=delete)
    delete_button.place(x=1200, y=135, width=49, height=43)

    edit_button = tk.Button(guimain, cursor="heart", image=iconeditadmin,font=("Times", 17), fg="#000000", justify="center", text="EDIT", borderwidth="3px", command=edit)
    edit_button.place(x=1200, y=200, width=49, height=43)

    label1 = tk.Label(guimain, cursor="heart", image=labelproduct)
    label1.place(x=360,y=70,width=156,height=30)

    label2 = tk.Label(guimain, cursor="heart", image=labelproduct)
    label2.place(x=360,y=140,width=156,height=30)
    
    label3 = tk.Label(guimain, cursor="heart", image=labelquantity)
    label3.place(x=360,y=210,width=156,height=30)


    products_listbox = tk.Listbox(guimain, bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 20), fg="#333333", relief="sunken")
    products_listbox.place(x=51, y=322, width=350, height=360)

    adminprice_listbox = tk.Listbox(guimain, bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 20), fg="#333333", relief="sunken")
    adminprice_listbox.place(x=401, y=322, width=300, height=360)

    adminquantity_listbox = tk.Listbox(guimain, bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 20), fg="#333333", relief="sunken")
    adminquantity_listbox.place(x=700, y=322, width=300, height=360)

    picture_listbox = tk.Listbox(guimain, bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 20), fg="#333333", relief="sunken")
    picture_listbox.place(x=1000, y=322, width=255, height=360)

    log = tk.Button(guimain, borderwidth="5px", cursor="heart", bg="#ffffff", fg="#000000", text="Log",command=logstore)
    log.place(x=1200, y=10, width=44, height=40)

    endadmin = tk.Button(guimain, borderwidth="5px", cursor="heart", bg="#FF0000", fg="#000000", text="X",command=back)
    endadmin.place(x=1250, y=10, width=44, height=40)
    show()
    
def pujudtum():
    def back():
        bg_pujudtum.destroy()
        endpujudtum.destroy()
    bg_pujudtum=tk.Label(guimain,image=pjt)
    bg_pujudtum.place(x=0,y=0,width=1306,height=697)
    endpujudtum = tk.Button(guimain,image=iconbackadmin, bg="#ff0000", font=("Times", 20), justify="center", borderwidth="0px", command=back)
    endpujudtum.place(x=940, y=17, width=49, height=43)

def loginadmin():
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def add_user(username, password):
        hashed_password = hash_password(password)
        cursor.execute('INSERT INTO admin (username, password, level, passwordnothast) VALUES (?,?,?,?)', (username, hashed_password,0, password))
        conn.commit()

    def add_user1():
        username = username_entry.get()
        password = password_entry.get()

        if username and password:
            add_user(username, password)
            messagebox.showinfo('เพิ่มผู้ใช้', 'เพิ่มผู้ใช้เรียบร้อยแล้ว!')

        else:
            messagebox.showerror('ข้อผิดพลาด', 'โปรดป้อนชื่อผู้ใช้และรหัสผ่านทั้งคู่.')
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        hashed_password = hash_password(password)
        cursor.execute('SELECT password FROM admin WHERE username = ?', (username,))
        result = cursor.fetchone()
        if result and result[0] == hashed_password:
            messagebox.showinfo('Login', '🔓Login successful!🔓')
            admin()
            closing()
        else:
            messagebox.showerror('Login', '🔒nvalid credentials.🔒')
            username_entry.delete(0,tk.END)
            password_entry.delete(0,tk.END)


    def closing():
        bglogin.destroy()
        username_entry.destroy()
        password_entry.destroy()
        add_user_button.destroy()
        login_button.destroy()
        exit_button.destroy()
    bglogin  = tk.Label(guimain, image=bghomepage, cursor="heart")
    bglogin.place(x=0, y=0, width=1306, height=697)

    username_entry = tk.Entry(guimain, bg="#ffffff", borderwidth="3px", cursor="heart", font=tkFont.Font(family='Times', size=20), fg="#000000", justify="center")
    username_entry.place(x=465, y=250, width=368, height=60)

    password_entry = tk.Entry(guimain, bg="#ffffff", borderwidth="3px", cursor="heart", font=tkFont.Font(family='Times', size=20),show='🔒', fg="#000000", justify="center")
    password_entry.place(x=465, y=330, width=368, height=60)

    add_user_button = tk.Button(guimain, bg="#CECE5A", cursor="heart", font=tkFont.Font(family='Times', size=18), fg="#000000", justify="center", text="REGISTER", relief="sunken",command=add_user1)
    add_user_button.place(x=680, y=430, width=150, height=50)

    login_button = tk.Button(guimain, bg="#CECE5A", cursor="heart", font=tkFont.Font(family='Times', size=18), fg="#000000", justify="center", text="LOGIN", relief="sunken",command=login)
    login_button.place(x=465, y=430, width=150, height=50)

    exit_button = tk.Button(guimain, borderwidth="5px", cursor="heart", bg="#FF0000", fg="#000000", text="X",command=closing)
    exit_button.place(x=1250, y=10, width=44, height=40)

def closeprogram():
    guimain.withdraw()

guimain = tk.Tk()
guimain.title("CLASSY STORE")
width=1306
height=697
screenwidth = guimain.winfo_screenwidth()
screenheight = guimain.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
guimain.geometry(alignstr)
guimain.resizable(width=False, height=False)

bghomepage = PhotoImage(file="E:\\project\\NEWNEW\\\CLASSYYY.png")
bgshop = PhotoImage(file="E:/project/GFGUI/homepage/buynow01.png")
bgbuttonadmin = PhotoImage(file="E:/project/GFGUI/homepage/admin01.png")
bgclose = PhotoImage(file="E:\project\GFGUI\homepage\close01.png")
bgiconcredit = PhotoImage(file="E:\project\GFGUI\homepage\Cr.png")

bgbuynow = PhotoImage(file="E:\\project\\NEWNEW\\SHOP.png")
bgiconback = PhotoImage(file="E:/project/GFGUI/buynow/back.png")
bgiconcart = PhotoImage(file="E:/project/GFGUI/buynow/cart.png")

blackgcart = PhotoImage(file="E:\project\\NEWNEW\CLASSYCART.png")
bgiconcartback = PhotoImage(file="E:/project/GFGUI/Cart/back.png")
bgicondelete = PhotoImage(file="E:\project\GFGUI\Cart\delete.png")
bgiconedit = PhotoImage(file="E:\project\GFGUI\Cart\edit.png")
bgiconpay = PhotoImage(file="E:\project\GFGUI\Cart\pay.png")
bgicontotalprice = PhotoImage(file="E:\project\GFGUI\Cart\price1.png")
bgiconeditnumber = PhotoImage(file="E:\project\GFGUI\Cart\editNumber.png")

bgadmin = PhotoImage(file="E:\\project\\NEWNEW\\admin.png")
iconaddadmin = PhotoImage(file="E:\\project\\GFGUI\\Admin\\add.png")
icondeleteadmin = PhotoImage(file="E:\project\GFGUI\Admin\delete.png")
iconeditadmin = PhotoImage(file="E:\project\GFGUI\Admin\edit.png")
iconbackadmin = PhotoImage(file="E:\\project\\GFGUI\\Admin\\back.png")
labelproduct = PhotoImage(file="E:\\project\\GFGUI\\Admin\\Product Name.png")
labelprice = PhotoImage(file="E:\\project\\GFGUI\\Admin\\Quantity.png")
labelquantity = PhotoImage(file="E:\\project\\GFGUI\\Admin\\Quantity.png")

pjt = PhotoImage(file="E:\project\\NEWNEW\jjj.png")
loginadminpic = PhotoImage(file="E:\project\GFGUI\loginadmin.png")

bgbill = PhotoImage(file="E:\project\\NEWNEW\BILL.png")

bgmain = tk.Label(guimain, bg="#ff99cc",image=bghomepage).place(x=0, y=0, width=1306, height=697)
buttonshop = tk.Button(guimain,bg="#ffffff",font=("Times", 22),text="SHOP NOW",borderwidth="5px",cursor="heart",fg="#000000",justify="center",relief="sunken", command=shop).place(x=550,y=260,width=206,height=64)
buttonadmin = tk.Button(guimain,bg="#ffffff",font=("Times", 22),text="ADMIN",borderwidth="5px",cursor="heart",fg="#000000",justify="center",relief="sunken",command=loginadmin).place(x=550,y=360,width=206,height=64)
buttonclose = tk.Button(guimain,bg="#ffffff",font=("Times", 22),text="CLOSE",borderwidth="5px",cursor="heart",fg="#000000",justify="center",relief="sunken",command=closeprogram).place(x=550,y=460,width=206,height=64)
buttoncredit = tk.Button(guimain, bg="#d8d8d8",image=bgiconcredit,cursor="heart",command=pujudtum).place(x=1250,y=30,width=44,height=40)
guimain.mainloop()
