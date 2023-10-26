import requests
import cv2
import numpy as np
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
def checkstock():
    checkstock=[]
    checkstock.clear
    cursor.execute("SELECT id,quantity FROM mystore")
    check = cursor.fetchall() 
    
    for x in check:
        checkstock.append(x[0])
    print(checkstock)
    c=0
    for y in check:
        if y[1] <=0 :
            print(checkstock[c])
            cursor.execute("DELETE FROM mystore WHERE id=?", (checkstock[c],))
            conn.commit()  
            c+=1
checkstock()