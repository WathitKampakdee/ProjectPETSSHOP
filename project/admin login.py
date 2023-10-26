import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import random
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import io
from datetime import datetime
from tkinter import messagebox
import tkinter as toplevel

def gamevoucher():
    x,y=400,400
    class SnakeGame:
        voucher=0
        def __init__(self, master, width, height):
            self.master = master
            self.width = width
            self.height = height
            self.bgsnakenoi = toplevel.Canvas(master, width=x, height=y,bg="black")
            self.bgsnakenoi.pack()
            self.setup_game()
            self.master.bind('<KeyPress>', self.on_keypress)
            self.controlsnake = 'Right'
            self.score = 0
            self.score_label = toplevel.Label(master, text="Score: 0")
            self.score_label.pack()
            self.move()
        def setup_game(self):
            self.snake = [(20,20)]
            self.food = self.generate_food()
            self.draw_snake()
            self.draw_food()
        def generate_food(self):
            x = random.randint(0, 19 ) * 20
            y = random.randint(0, 19) * 20
            return (x, y)      
        def draw_snake(self):
            self.bgsnakenoi.delete('snake')
            for segment in self.snake:
                x, y = segment
                self.bgsnakenoi.create_rectangle(x, y, x + 20, y + 20, fill='blue', tags='snake')
        def draw_food(self):
            self.bgsnakenoi.delete('food')
            x, y = self.food
            self.bgsnakenoi.create_rectangle(x, y, x + 20, y + 20, fill='pink', tags='food')
        def move(self):
            head = self.snake[-1]
            if self.controlsnake == 'Up':
                new_head = (head[0], head[1] - 20)
            elif self.controlsnake == 'Down':
                new_head = (head[0], head[1] + 20)
            elif self.controlsnake == 'Left':
                new_head = (head[0] - 20, head[1])
            elif self.controlsnake == 'Right':
                new_head = (head[0] + 20, head[1])
            self.snake.append(new_head)
            if new_head == self.food:  
                self.food = self.generate_food()
                self.draw_food()
                self.score += 10
                self.update_score()
            else:
                self.snake.pop(0)
            self.draw_snake()
            self.check_collision()
            self.master.after(40, self.move)
        def check_collision(self):
            head = self.snake[-1]
            if head in self.snake[:-1] or head[0] < 0 or head[0] >= self.width or head[1] < 0 or head[1] >= self.height:
                print("Game Over")
                voucher=self.score
                print(voucher)
                self.master.destroy()
        def update_score(self):
            self.score_label.config(text="Score: {}".format(self.score))
        def on_keypress(self,cont):
            key = cont.keysym
            if (key == 'Up' and self.controlsnake != 'Down') or (key == 'Down' and self.controlsnake != 'Up') or (key == 'Left' and self.controlsnake != 'Right') or (key == 'Right' and self.controlsnake != 'Left'):
                self.controlsnake = key
    snakegamegui = toplevel.Tk()
    snakegamegui.title("Snake Game")
    game = SnakeGame(snakegamegui, width=x,height=y)
    snakegamegui.mainloop()
def game():
    x,y=400,400
    class SnakeGame:
        voucher=0
        def __init__(self, master, width, height):
            self.master = master
            self.width = width
            self.height = height
            self.canvas = toplevel.Canvas(master, width=x, height=y,bg="black")
            self.canvas.pack()
            self.setup_game()
            self.master.bind('<KeyPress>', self.on_keypress)
            self.controlsnake = 'Right'
            self.score = 0
            self.score_label = toplevel.Label(master, text="Score: 0")
            self.score_label.pack()
            self.move()
        def setup_game(self):
            self.snake = [(20,20)]
            self.food = self.generate_food()
            self.draw_snake()
            self.draw_food()
        def generate_food(self):
            x = random.randint(0, 19 ) * 20
            y = random.randint(0, 19) * 20
            return (x, y)      
        def draw_snake(self):
            self.canvas.delete('snake')
            for segment in self.snake:
                x, y = segment
                self.canvas.create_rectangle(x, y, x + 20, y + 20, fill='blue', tags='snake')
        def draw_food(self):
            self.canvas.delete('food')
            x, y = self.food
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill='pink', tags='food')
        def move(self):
            head = self.snake[-1]
            if self.controlsnake == 'Up':
                new_head = (head[0], head[1] - 20)
            elif self.controlsnake == 'Down':
                new_head = (head[0], head[1] + 20)
            elif self.controlsnake == 'Left':
                new_head = (head[0] - 20, head[1])
            elif self.controlsnake == 'Right':
                new_head = (head[0] + 20, head[1])
            self.snake.append(new_head)
            if new_head == self.food:  
                self.food = self.generate_food()
                self.draw_food()
                self.score += 10
                self.update_score()
            else:
                self.snake.pop(0)
            self.draw_snake()
            self.check_collision()
            self.master.after(40, self.move)
        def check_collision(self):
            head = self.snake[-1]
            if head in self.snake[:-1] or head[0] < 0 or head[0] >= self.width or head[1] < 0 or head[1] >= self.height:
                print("Game Over")
                voucher=self.score
                print(voucher)
                self.master.destroy()
        def update_score(self):
            self.score_label.config(text="Score: {}".format(self.score))
        def on_keypress(self,cont):
            key = cont.keysym
            if (key == 'Up' and self.controlsnake != 'Down') or (key == 'Down' and self.controlsnake != 'Up') or (key == 'Left' and self.controlsnake != 'Right') or (key == 'Right' and self.controlsnake != 'Left'):
                self.controlsnake = key
    snakegamegui = toplevel.Tk()
    snakegamegui.title("Snake Game")
    game = SnakeGame(snakegamegui, width=x,height=y)
    snakegamegui.mainloop()

def checkint(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False 
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
            i=1

            tempidproduct.clear()
            for x in result:
                products_listbox.insert(x[0],"           {}    ".format(x[1]))
                adminprice_listbox.insert(x[0],"       {}  THB   ".format(x[2])) 
                adminquantity_listbox.insert(x[0],"         {}    ".format(x[3]))  
                picture_listbox.insert(x[0]," {}    ".format(x[4]))   
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
        products_listbox.destroy()
        adminprice_listbox.destroy()
        adminquantity_listbox.destroy()
        picture_listbox.destroy()
        endadmin.destroy() 
  
    bg_color=tk.Label(root,image=bgadmin)
    bg_color.place(x=0,y=0,width=1017,height=725)
    name_entry = tk.Entry(root, bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 10), fg="#000000", justify="center", relief="sunken")
    name_entry.place(x=527,y=63,width=303,height=31)
    validate_func = root.register(checkint)
    price_entry=tk.Entry(root,validate='key',validatecommand=(validate_func, "%P"),bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 10), fg="#000000", justify="center", relief="sunken")
    price_entry.place(x=527,y=125,width=303,height=31)
    quantity_entry=tk.Entry(root,validate='key',validatecommand=(validate_func, "%P"),bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 10), fg="#000000", justify="center", relief="sunken")
    quantity_entry.place(x=527,y=190,width=303,height=31)

    add_button = tk.Button(root, cursor="heart", image=iconaddadmin, font=("Times", 17), fg="#000000", justify="center", text="ADD",  borderwidth="3px", command=add)
    add_button.place(x=840, y=56, width=49, height=43)

    delete_button = tk.Button(root, cursor="heart", image=icondeleteadmin, font=("Times", 17), fg="#000000", justify="center", text="DELETE", borderwidth="3px", command=delete)
    delete_button.place(x=840, y=120, width=49, height=43)

    edit_button = tk.Button(root, cursor="heart", image=iconeditadmin,font=("Times", 17), fg="#000000", justify="center", text="EDIT", borderwidth="3px", command=edit)
    edit_button.place(x=840, y=185, width=49, height=43)

    products_listbox = tk.Listbox(root, bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
    products_listbox.place(x=43, y=325, width=350, height=360)

    adminprice_listbox = tk.Listbox(root, bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
    adminprice_listbox.place(x=393, y=325, width=185, height=360)

    adminquantity_listbox = tk.Listbox(root, bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
    adminquantity_listbox.place(x=578, y=325, width=350, height=360)

    picture_listbox = tk.Listbox(root, bg="#ffffff", borderwidth="1px", cursor="heart", font=("Times", 14), fg="#333333", relief="sunken")
    picture_listbox.place(x=763, y=325, width=210, height=360)

    endadmin = tk.Button(root,image=iconbackadmin, bg="#ff0000", font=("Times", 20), justify="center", borderwidth="0px", command=back)
    endadmin.place(x=940, y=17, width=49, height=43)
    show()


root = tk.Tk()
root.title("CLASSY STORE")
width=1019
height=730
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

bghomepage = PhotoImage(file="E:\project\GFGUI\homepage\homepage.png")
bgshop = PhotoImage(file="E:/project/GFGUI/homepage/buynow01.png")
bgbuttonadmin = PhotoImage(file="E:/project/GFGUI/homepage/admin01.png")
bgclose = PhotoImage(file="E:\project\GFGUI\homepage\close01.png")
bgiconcredit = PhotoImage(file="E:\project\GFGUI\homepage\Cr.png")

bgbuynow = PhotoImage(file="E:/project/GFGUI/buynow/buynowbg.png")
bgiconback = PhotoImage(file="E:/project/GFGUI/buynow/back.png")
bgiconcart = PhotoImage(file="E:/project/GFGUI/buynow/cart.png")

blackgcart = PhotoImage(file="E:\project\GFGUI\Cart\BG.png")
bgiconcartback = PhotoImage(file="E:/project/GFGUI/Cart/back.png")
bgicondelete = PhotoImage(file="E:\project\GFGUI\Cart\delete.png")
bgiconedit = PhotoImage(file="E:\project\GFGUI\Cart\edit.png")
bgiconpay = PhotoImage(file="E:\project\GFGUI\Cart\pay.png")
bgicontotalprice = PhotoImage(file="E:\project\GFGUI\Cart\price1.png")
bgiconeditnumber = PhotoImage(file="E:\project\GFGUI\Cart\editNumber.png")

bgadmin = PhotoImage(file="E:\project\GFGUI\Admin\BG.png")
iconaddadmin = PhotoImage(file="E:\\project\\GFGUI\\Admin\\add.png")
icondeleteadmin = PhotoImage(file="E:\project\GFGUI\Admin\delete.png")
iconeditadmin = PhotoImage(file="E:\project\GFGUI\Admin\edit.png")
iconbackadmin = PhotoImage(file="E:\\project\\GFGUI\\Admin\\back.png")


bgmain = tk.Label(root, bg="#ff99cc",image=bghomepage).place(x=0, y=0, width=1017, height=730)
buttonadmin = tk.Button(root, bg="#d8d8d8",image=bgbuttonadmin,cursor="heart",command=admin).place(x=620, y=310, width=256, height=67)
root.mainloop()