import cv2
from tkinter import *
import sqlite3
from datetime import datetime,timedelta 
from tkinter import *
from tkinter import Tk, Label ,ttk
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.messagebox
import requests
from io import BytesIO
import numpy as np


#สร้าง QR ล็อกเงิน
root=Tk()
root.title("แมว")
root.geometry("100x300")
main=Image.open(r'D:\coding\project\pj\showcusid55.png')
root.b=ImageTk.PhotoImage(main)
Label(root,image=root.b).place(x=0,y=0)
sum=2
text = "https://promptpay.io/0953929205/" + str(sum) + ".png"
image_url = text


response = requests.get(image_url)

if response.status_code == 200:
    image = Image.open(BytesIO(response.content))
    
    
    if image.mode != 'L':
        image = image.convert('L')

    img_np = np.array(image)

    qr_decoder = cv2.QRCodeDetector()

    
    val, pts, qr_code = qr_decoder.detectAndDecode(img_np)

    image = image.resize((int(image.width*0.5),int(image.height*0.5)))
    img_tk = ImageTk.PhotoImage(image)
    qr = Label(root, image=img_tk)
    qr.image = img_tk  
    qr.place(x = 0, y = 0)

else:
    print("Failed to download the image. HTTP status code:", response.status_code)
root.mainloop()