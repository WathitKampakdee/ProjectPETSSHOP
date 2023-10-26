import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import random

conn = sqlite3.connect(r"E:\project\databeta.db")
cursor = conn.cursor()

def display_show_product():
    cursor.execute("SELECT * FROM mystore")
    pictures = cursor.fetchall()
    
    def addtocart(item):
        def add():
            c = conn.cursor()
            c.execute("INSERT INTO myorder (name, price, quantity, picture) VALUES (?, ?, ?, ?)", (item[1], item[2], item[3], item[4]))
            conn.commit()
        return add

    for i, x in enumerate(pictures):
        image = Image.open(BytesIO(x[4]))
        target_width, target_height = 128, 128
        image = image.resize((target_width, target_height))
        image = ImageTk.PhotoImage(image)


        label = Button(product, image=image, text=" {}  $ {} ".format(x[1], x[2]), compound="top", command=addtocart(x), bg= "#000000", fg="#ffffff")
        label.image = image
        label.grid(row=i // 6, column=i % 6, padx=10, pady=10)

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

root = Tk()
root.title("CLASSY SHOP")
width = 1019
height = 730
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

imagebg = PhotoImage(file="E:\project\IMAGE BG\ROSE.png")
m = PhotoImage(file="E:\project\IMAGE BG\mm.png")
i = PhotoImage(file="E:\project\IMAGE BG\CCC.png")
c = PhotoImage(file="E:\project\IMAGE BG\CLASSY.png")

bgorder = Label(root, bg="#c71585",image=imagebg,cursor="heart")
bgorder.place(x=0, y=0, width=1019, height=730)

namestore=Label(root,image=c)
namestore.place(x=250,y=25,width=498,height=66)

cart = Button(root, bg="#ffffff", cursor="heart",image=i, fg="#000000", justify="center",  relief="groove", borderwidth="1px")
cart.place(x=830,y=30, width=65, height=55)

end_order = Button(root, bg="#ff0000", cursor="heart", font=("Times", 20), justify="center", text="X", borderwidth="2px")
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
