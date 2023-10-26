import requests
import cv2
import numpy as np
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import random
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from datetime import datetime
from tkinter import messagebox
import tkinter as toplevel
import hashlib


def pay():
    scan =sumpay
    text = "https://promptpay.io/0611100728/" + str(scan) + ".png"
    image_url = text

    response = requests.get(image_url)

    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))

        if image.mode != 'L':
            image = image.convert('L')

        image = image.resize((00, 100))  
        img_tk = ImageTk.PhotoImage(image)

        lebel_qr = Label(hh, image=img_tk)
        lebel_qr.image = img_tk 
        lebel_qr.place(x=0, y=0)

    else:
        print("Failed to download the image. HTTP status code:", response.status_code)


guimain = tk.Tk()
guimain.title("CLASSY STORE")
width=1306
height=697
screenwidth = guimain.winfo_screenwidth()
screenheight = guimain.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
guimain.geometry(alignstr)
guimain.resizable(width=False, height=False)

hh=Label(guimain,bg="#000000")
hh.place(x=0,y=0,width=300,height=300)


buttonshop = tk.Button(guimain,bg="#ffffff",font=("Times", 22),text="SHOP NOW",borderwidth="5px",cursor="heart",fg="#000000",justify="center",relief="sunken", command=pay)
buttonshop.place(x=550,y=260,width=206,height=64)

guimain.mainloop()



