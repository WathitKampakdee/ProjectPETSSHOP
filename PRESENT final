import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import sqlite3
from datetime import datetime
from PIL import Image, ImageTk
class PetShopPOS:
    def __init__(self, root):
        self.root = root
        self.root.title("ระบบขายสินค้าร้านขายอาหารสัตว์เลี้ยง")
        self.root.geometry("1280x720")
        bg_image = Image.open("OG.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.root, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.password = "1234"
        self.selected_items = {}
        self.total_price = tk.DoubleVar()
 
        self.menu = [
            {"animal": "Dog", "food": "หูกระต่ายอบแห้ง", "price": 50, "stock": 100, "image": None},
            {"animal": "Dog", "food": "อาหารเม็ด", "price": 30, "stock": 100, "image": None},
            {"animal": "Dog", "food": "อาหารดิบ", "price": 40, "stock": 100, "image": None},
            {"animal": "Cat", "food": "Meo", "price": 20, "stock": 100, "image": None},
            {"animal": "Cat", "food": "เเมวเลีย", "price": 10, "stock": 100, "image": None},
            {"animal": "Cat", "food": "ปลากระป๋อง", "price": 50, "stock": 100, "image": None},
            {"animal": "Hamster", "food": "เมล็ดทานตะวัน", "price": 10, "stock": 100, "image": None},
            {"animal": "Cow", "food": "ฟาง", "price": 30, "stock": 100, "image": None}
        ]
        
        self.load_images()
        self.create_gui()

        # Connect to SQLite database
        self.conn = sqlite3.connect("sales_database.db")
        self.create_sales_table()
        self.create_items_table()
        
      
        # เพิ่มส่วนนี้เพื่อสร้างหน้า Login เมื่อเปิดโปรแกรม
        self.login_page()
                
    def login_page(self):
        # สร้าง GUI สำหรับหน้า Login
        self.hide_main_window()  # ซ่อนหน้าหลัก
        

        login_frame = tk.Frame(self.root, padx=20, pady=20)
        login_frame.pack(expand=True, fill=tk.BOTH)

        tk.Label(login_frame, text="กรุณากรอกหมายเลขโทรศัพท์เพื่อเข้าสู่ระบบ", font=("Arial", 16)).pack(pady=10)
        phone_entry = tk.Entry(login_frame, font=("Arial", 14))
        phone_entry.pack(pady=10)

        login_button = tk.Button(login_frame, text="เข้าสู่ระบบ", command=lambda: self.verify_login(phone_entry.get()), font=("Arial", 14),width=18)
        login_button.pack(pady=20)

        # เพิ่มปุ่มสำหรับไปที่หน้าสมัครสมาชิกใหม่
        register_button = tk.Button(login_frame, text="สมัครสมาชิกใหม่", command=self.register_page, font=("Arial", 14),width=18)
        register_button.pack()
          
    def verify_login(self, phone_number):
    # ตรวจสอบหมายเลขโทรศัพท์ในฐานข้อมูล SQLite
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE phone=?", (phone_number,))
        customer_data = cursor.fetchone()
        cursor.close()

        if phone_number == "":
        # ถ้าหมายเลขโทรศัพท์ว่างเปล่า
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกหมายเลขโทรศัพท์")
        elif customer_data:
        # ถ้าพบหมายเลขโทรศัพท์ในฐานข้อมูล
        # สร้างหน้าหลักใหม่และซ่อนหน้า login
            self.create_gui()
        else:
        # ถ้าไม่พบหมายเลขโทรศัพท์ในฐานข้อมูล
        # แสดงข้อความผิดพลาด
            messagebox.showerror("ข้อผิดพลาด", "หมายเลขโทรศัพท์ไม่ถูกต้อง")

    def register_page(self):
        # สร้าง GUI สำหรับหน้าสมัครสมาชิกใหม่
        register_frame = tk.Frame(self.root, padx=20, pady=20)
        register_frame.pack(expand=True, fill=tk.BOTH)

        tk.Label(register_frame, text="กรุณากรอกชื่อลูกค้า", font=("Arial", 16)).pack(pady=10)
        name_entry = tk.Entry(register_frame, font=("Arial", 14))
        name_entry.pack(pady=10)

        tk.Label(register_frame, text="กรุณากรอกหมายเลขโทรศัพท์", font=("Arial", 16)).pack(pady=10)
        phone_entry = tk.Entry(register_frame, font=("Arial", 14))
        phone_entry.pack(pady=10)

        register_button = tk.Button(register_frame, text="ลงทะเบียน", command=lambda: self.save_customer_data(name_entry.get(), phone_entry.get()), font=("Arial", 14))
        register_button.pack(pady=20)

    def save_customer_data(self, name, phone):
        # ตรวจสอบว่าชื่อถูกกรอกหรือไม่
        if not name:
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกชื่อลูกค้า")
            return

        # ตรวจสอบว่าหมายเลขโทรศัพท์ถูกกรอกหรือไม่
        if not phone:
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกหมายเลขโทรศัพท์")
            return

        # ตรวจสอบว่าหมายเลขโทรศัพท์นี้ถูกใช้ไปแล้วหรือไม่
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM customers WHERE phone=?", (phone,))
        existing_customer = cursor.fetchone()
        cursor.close()

        if existing_customer:
            messagebox.showerror("ข้อผิดพลาด", "หมายเลขโทรศัพท์นี้ถูกใช้ไปแล้ว")
            return

        # บันทึกข้อมูลลูกค้าในฐานข้อมูล SQLite
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?)", (name, phone))
        self.conn.commit()
        cursor.close()

        # แสดงข้อความยืนยันการบันทึกข้อมูล
        messagebox.showinfo("สำเร็จ", "บันทึกข้อมูลลูกค้าเรียบร้อยแล้ว")

    
                      
    # โหลดรูปภาพสินค้าจากไฟล์และเก็บไว้ในตัวแปร    
    def load_images(self):
        self.image_meo = self.load_image("1.png")
        self.image_pla_krapong = self.load_image("2.png")
        self.image_melon_seeds = self.load_image("3.png")
        self.image_raw_food = self.load_image("5.png")
        self.image_dry_food = self.load_image("6.png")
        self.image_dried_rabbit_ear = self.load_image("4.png")
        self.image_mewlia = self.load_image("7.png")
        self.image_fang = self.load_image("fff.png")
    # โหลดไฟล์รูปภาพและแปลงเป็น ImageTk.PhotoImage
    def load_image(self, filename):
        try:
            image = Image.open(filename)
            photo_image = ImageTk.PhotoImage(image)
            image.close()
            return photo_image
        except Exception as e:
            print(f"Error loading image {filename}: {e}")
            return None
            
    # สร้างหน้า GUI หลักที่มีปุ่มต่าง ๆ  เริ่มการซื้อขาย, เพิ่มรายการสินค้าใหม่, จัดการสต็อก, แสดงข้อมูลผู้สร้าง และปุ่มออกจากโปรแกรม
    def create_gui(self):
        
        self.welcome_label = tk.Label(self.root, text="ยินดีต้อนรับสู่ร้านขายอาหารสัตว์เลี้ยง", font=("Arial", 24), bg="brown", fg="white")
        self.welcome_label.pack(pady=20)

        bg_image = Image.open("OG.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.root, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        

        self.start_shopping_button = tk.Button(self.root, text="เริ่มเลือกสินค้าและชำระเงิน", command=self.start_shopping, font=("Arial", 16),width=18)
        self.start_shopping_button.pack()

        self.admin_label = tk.Label(self.root, text="Admin", font=("Arial", 16))
        self.admin_label.pack()

        self.add_item_button = tk.Button(self.root, text="เพิ่มรายการอาหารใหม่", command=self.add_item_with_image, font=("Arial", 16),width=18)
        self.add_item_button.pack()

        self.stock_button = tk.Button(self.root, text="จัดการสต็อกสินค้า", command=self.manage_stock, font=("Arial", 16),width=18)
        self.stock_button.pack()

        self.creator_button = tk.Button(self.root, text="ผู้สร้าง", command=self.show_creator_info, font=("Arial", 16),width=18)
        self.creator_button.pack()

        self.sales_button = tk.Button(self.root, text="ดูยอดขายรายวัน", command=self.show_sales_details, font=("Arial", 16),width=18)
        self.sales_button.pack()

        self.exit_button = tk.Button(self.root, text="ออก", command=self.exit_program, font=("Arial", 16), bg="red", fg="white",width=18)
        self.exit_button.pack()

        self.edit_customer_button = tk.Button(self.root, text="เเก้ไขข้อมูลลูกค้า", command=self.edit_customer_gui, font=("Arial", 16),width=18)
        self.edit_customer_button.pack()

        self.edit_customer_button.place(relx=0.5, rely=0.82, anchor=tk.CENTER)
        self.start_shopping_button.place(relx=0.5, rely=0.30, anchor=tk.CENTER)
        self.admin_label.place(relx=0.5, rely=0.44, anchor=tk.CENTER)
        self.add_item_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.stock_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        self.sales_button.place(relx=0.5, rely=0.67, anchor=tk.CENTER)
        self.creator_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        self.exit_button.place(relx=0.5, rely=0.89, anchor=tk.CENTER)

    def start_shopping(self):
        self.hide_main_window()
        self.create_shopping_gui()

    def create_shopping_gui(self):
        self.destroy_shopping_gui()  # ทำลายหน้า GUI ที่มีอยู่
        main_frame = tk.Frame(self.root, bg="light blue")
        main_frame.pack(expand=True, fill=tk.BOTH)

        left_frame = tk.Frame(main_frame, bg="light blue", width=500)
        left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH)

        right_frame = tk.Frame(main_frame, bg="light blue")
        right_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.BOTH)

        animal_groups = {}
        for item in self.menu:
            animal = item["animal"]
            if animal not in animal_groups:
                animal_groups[animal] = []
            animal_groups[animal].append(item)
        # คือการดึงคีย์ (ชื่อของสัตว์) จากพจนานุกรม
        sorted_animals = sorted(animal_groups.keys())

        tk.Label(left_frame, text="เลือกสินค้า", font=("Arial", 16)).pack()
        self.item_buttons = []

        # สร้าง Canvas และ Scrollbar ใน left_frame
        canvas = tk.Canvas(left_frame, bg="light blue", width=500)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # สร้างscrollbar
        scrollbar = tk.Scrollbar(left_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # กำหนดคำสั่งให้ Canvas ใช้ Scrollbar ในแนวตั้งเพื่อเลื่อนเนื้อหาขึ้นหรือลง.
        canvas.configure(yscrollcommand=scrollbar.set)

        # สร้างเฟรมภายในแคนวาสเพื่อเก็บรายการสินค้า
        items_frame = tk.Frame(canvas, bg="light blue")
        canvas.create_window((0, 0), window=items_frame, anchor=tk.NW)

        for animal in sorted_animals:
            tk.Label(items_frame, text=f"{animal}:", font=("Arial", 14), bg="light blue").pack(anchor=tk.W)
            sorted_items = sorted(animal_groups[animal], key=lambda x: x['food'])
            for item_data in sorted_items:
                item_frame = tk.Frame(items_frame, bg="light blue")
                item_frame.pack(fill=tk.X, pady=5)
                
                item_image = self.get_item_image(item_data)
                if item_image:
                    item_image_label = tk.Label(item_frame, image=item_image, padx=5)
                    item_image_label.image = item_image
                    item_image_label.pack(side=tk.LEFT)

                item_label = tk.Label(item_frame, text=f"{item_data['food']}: {item_data['price']} บาท (สต็อก: {item_data['stock']})", font=("Arial", 12), bg="light blue")
                item_label.pack(side=tk.LEFT, padx=10)

                remove_from_cart_button = tk.Button(item_frame, text="-", command=lambda item=item_data: self.remove_from_cart(item), font=("Arial", 12))
                remove_from_cart_button.pack(side=tk.RIGHT)
                
                add_to_cart_button = tk.Button(item_frame, text="+", command=lambda item=item_data: self.add_to_cart(item), font=("Arial", 12))
                add_to_cart_button.pack(side=tk.RIGHT)

            

                self.item_buttons.append(add_to_cart_button)

        # ผูกการเลื่อนหน้าต่าง Canvasกับเมาส์
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1*(event.delta//120), "units"))

        # ตระกร้าสินค้า
        tk.Label(right_frame, text="ตะกร้าสินค้า", font=("Arial", 16)).pack()
        self.cart_listbox = tk.Listbox(right_frame, font=("Arial", 12))
        self.cart_listbox.pack(fill=tk.BOTH, expand=True)

        self.total_price_label = tk.Label(right_frame, text="ราคารวม: 0 บาท", font=("Arial", 14))
        self.total_price_label.pack()

        checkout_button = tk.Button(right_frame, text="ชำระเงิน", command=self.checkout, font=("Arial", 16), bg="green", fg="white",width=10)
        checkout_button.pack()

        clear_cart_button = tk.Button(right_frame, text="ล้างตะกร้า", command=self.clear_cart, font=("Arial", 16), bg="red", fg="white",width=10)
        clear_cart_button.pack()


        back_button = tk.Button(right_frame, text="กลับ", command=self.go_back, font=("Arial", 16),width=10)
        back_button.pack()
    
    def get_item_image(self, item_data):
        if item_data.get("image"):
            return item_data["image"]
        elif item_data["food"] == "Meo":
            return self.image_meo
        elif item_data["food"] == "ปลากระป๋อง":
            return self.image_pla_krapong
        elif item_data["food"] == "เมล็ดทานตะวัน":
            return self.image_melon_seeds
        elif item_data["food"] == "อาหารดิบ":
            return self.image_raw_food
        elif item_data["food"] == "อาหารเม็ด":
            return self.image_dry_food
        elif item_data["food"] == "หูกระต่ายอบแห้ง":
            return self.image_dried_rabbit_ear
        elif item_data["food"] == "เเมวเลีย":
            return self.image_mewlia
        elif item_data["food"] == "ฟาง":
            return self.image_fang
        else:
            return None
    # เพิ่มสินค้าลงในตะกร้าและแสดงข้อมูลในตะกร้า
    def add_to_cart(self, item_data):
        if item_data["food"] not in self.selected_items:
            if item_data["stock"] > 0:
                self.selected_items[item_data["food"]] = {
                    "item_data": item_data,
                    "quantity": tk.IntVar(value=1),
                    "total_price": item_data["price"]
                }
                item_data["stock"] -= 1  # ลดจำนวนสต็อกของสินค้าที่ถูกเพิ่มในตะกร้า
            else:
                messagebox.showwarning("สินค้าหมด", f"สินค้า {item_data['food']} หมดสต็อกแล้ว")
        else:
            selected_item = self.selected_items[item_data["food"]]
            if item_data["stock"] > 0 and selected_item["quantity"].get() < item_data["stock"]:
                selected_item["quantity"].set(selected_item["quantity"].get() + 1)
                selected_item["total_price"] = selected_item["quantity"].get() * item_data["price"]
                item_data["stock"] -= 1  # ลดจำนวนสต็อกของสินค้าที่ถูกเพิ่มในตะกร้า
            elif item_data["stock"] <= 0:
                messagebox.showwarning("สินค้าหมด", f"สินค้า {item_data['food']} หมดสต็อกแล้ว")
            else:
                messagebox.showwarning("จำนวนสินค้าเกิน", f"สินค้า {item_data['food']} มีจำนวนในสต็อกไม่เพียงพอ")

        self.update_cart_listbox()
        self.calculate_total_price()

    def remove_from_cart(self, item_data):
        if item_data["food"] in self.selected_items:
            selected_item = self.selected_items[item_data["food"]]
            selected_item["quantity"].set(selected_item["quantity"].get() - 1)
            if selected_item["quantity"].get() <= 0:
                del self.selected_items[item_data["food"]]
                item_data["stock"] += 1  # เพิ่มจำนวนสต็อกของสินค้าที่ถูกลบออกจากตะกร้า
            else:
                selected_item["total_price"] = selected_item["quantity"].get() * item_data["price"]
                item_data["stock"] += 1  # เพิ่มจำนวนสต็อกของสินค้าที่ถูกลบออกจากตะกร้า
            self.update_cart_listbox()
            self.calculate_total_price()

    # อัปเดตรายการสินค้าในตะกร้า
    def update_cart_listbox(self):
        self.cart_listbox.delete(0, tk.END)
        for item_name, selected_item in self.selected_items.items():
            quantity = selected_item["quantity"].get()
            if quantity > 0:
                self.cart_listbox.insert(tk.END, f"{selected_item['item_data']['food']} x{quantity} = {selected_item['total_price']} บาท (สต็อก: {selected_item['item_data']['stock']})") 
                
    # คำนวณราคารวมของสินค้าทั้งหมดในตะกร้า
    def calculate_total_price(self):
        total_price = sum(selected_item["total_price"] for selected_item in self.selected_items.values())
        self.total_price.set(total_price)
        self.total_price_label.config(text=f"ราคารวม: {total_price} บาท")

    # ดำเนินการชำระเงิน, บันทึกรายการขายในฐานข้อมูล SQLite, แสดงใบเสร็จ
    def checkout(self):
        if not self.selected_items:
            messagebox.showerror("ข้อผิดพลาด", "โปรดเลือกสินค้าก่อนทำการชำระเงิน")
            return
        # กรอกข้อมูลลูกค้า
        customer_name, customer_phone = self.get_customer_details() 
        if not customer_name or not customer_phone:
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกชื่อลูกค้าและเบอร์โทรศัพท์")
            return

        transaction_id = datetime.now().strftime("%Y%m%d%H%M")
        items_details = "\n".join([f"{item_name} x{selected_item['quantity'].get()} = {selected_item['total_price']} บาท" for item_name, selected_item in self.selected_items.items()])
        total_price = self.total_price.get()
        
        # Save sale data to the SQLite database
        self.save_sale_to_database(transaction_id, customer_name, customer_phone, items_details, total_price)

        # อัปเดตจำนวนสินค้าในฐานข้อมูล SQLite
        self.update_items_stock()

        self.show_receipt(transaction_id, customer_name, customer_phone)
        messagebox.showinfo("สำเร็จ", "ชำระเงินเรียบร้อยแล้ว")
        
    # ที่จะอัปเดตข้อมูลจำนวนสินค้าในฐานข้อมูล SQLite:
    def update_items_stock(self):
        for item_name, selected_item in self.selected_items.items():
            # ดึงข้อมูลสินค้าปัจจุบันจาก SQLite
            cursor = self.conn.cursor()
            cursor.execute("SELECT stock FROM items WHERE name=?", (item_name,))
            current_stock = cursor.fetchone()[0]
            cursor.close()

            # อัปเดตจำนวนสินค้าใน SQLite เป็นคงเหลือล่าสุด
            updated_stock = current_stock - selected_item['quantity'].get()
            cursor = self.conn.cursor()
            cursor.execute("UPDATE items SET stock=? WHERE name=?", (updated_stock, item_name))
            self.conn.commit()
            cursor.close()


    # บันทึกข้อมูลการขายลงในฐานข้อมูล SQLite
    def save_sale_to_database(self, transaction_id, customer_name, customer_phone, items_details, total_price):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO sales (transaction_id, customer_name, customer_phone, timestamp, items_details, total_price)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (transaction_id, customer_name, customer_phone, datetime.now(), items_details, total_price))
        self.conn.commit()
    # แสดงใบเสร็จการซื้อสินค้า
    def show_receipt(self, transaction_id, customer_name, customer_phone):
        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("ใบเสร็จ")
        receipt_window.geometry("400x500")

        receipt_frame = tk.Frame(receipt_window, padx=20, pady=20)
        receipt_frame.pack(expand=True, fill=tk.BOTH)

        tk.Label(receipt_frame, text="ใบเสร็จ", font=("Arial", 24)).pack()
        tk.Label(receipt_frame, text=f"เลขที่รายการ: {transaction_id}", font=("Arial", 14)).pack()

        tk.Label(receipt_frame, text="ลูกค้า: " + customer_name, font=("Arial", 14)).pack()
        tk.Label(receipt_frame, text="เบอร์โทร: " + customer_phone, font=("Arial", 14)).pack()

        tk.Label(receipt_frame, text="วันที่และเวลา: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"), font=("Arial", 14)).pack()

        tk.Label(receipt_frame, text="รายการสินค้า:", font=("Arial", 16)).pack()
        for item_name, selected_item in self.selected_items.items():
            quantity = selected_item["quantity"].get()
            if quantity > 0:
                tk.Label(receipt_frame, text=f"{item_name} x{quantity} = {selected_item['total_price']} บาท", font=("Arial", 14)).pack()

        tk.Label(receipt_frame, text="ราคารวม: " + str(self.total_price.get()) + " บาท", font=("Arial", 14)).pack()
    # รับข้อมูลชื่อลูกค้าและเบอร์โทรศัพท์จากผู้ใช้
    def get_customer_details(self):
        customer_name = simpledialog.askstring("ระบุข้อมูลลูกค้า", "ชื่อลูกค้า:")
        customer_phone = simpledialog.askstring("ระบุข้อมูลลูกค้า", "เบอร์โทรศัพท์:")

        # ตรวจสอบว่าเบอร์โทรศัพท์ที่ป้อนเข้ามาเป็นตัวเลขหรือไม่
        while not customer_phone.isdigit():
            messagebox.showerror("ข้อผิดพลาด", "โปรดกรอกเบอร์โทรศัพท์เป็นตัวเลขเท่านั้น")
            customer_phone = simpledialog.askstring("ระบุข้อมูลลูกค้า", "เบอร์โทรศัพท์:")

        return customer_name, customer_phone

    # ล้างสินค้าในตะกร้า
    def clear_cart(self):
        self.selected_items.clear()
        self.cart_listbox.delete(0, tk.END)
        self.calculate_total_price()
    # กลับไปยังหน้าหลัก
    def go_back(self):
        self.destroy_shopping_gui()  
        self.create_gui()  # สร้างหน้า GUI หลัก
        # self.show_main_window()  # แสดงหน้าหลักใหม่

    def manage_stock(self):
        # ตรวจสอบรหัสผ่านก่อนที่จะเปิดหน้าต่าง "จัดการสต็อกสินค้า"
        password_input = simpledialog.askstring("รหัสผ่าน", "กรุณากรอกรหัสผ่าน (4 หลัก):", show="*")
        if password_input == "1234":
            stock_window = tk.Toplevel(self.root)
            stock_window.title("จัดการสต็อกสินค้า")
            stock_window.geometry("500x500")

            stock_label = tk.Label(stock_window, text="กรุณาเลือกสินค้าที่ต้องการจัดการสต็อก", font=("Arial", 20))
            stock_label.pack(pady=10)
            
            item_var = tk.StringVar()
            items = [item["food"] for item in self.menu]
            item_menu = tk.OptionMenu(stock_window, item_var, *items)
            item_menu.pack(pady=10)

            selected_item_label = tk.Label(stock_window, text="จำนวนสินค้าในสต็อก:", font=("Arial", 18))
            selected_item_label.pack()
        else:
            messagebox.showerror("ข้อผิดพลาด", "รหัสผ่านไม่ถูกต้อง")
    # สร้างตัวแปรเพื่อเก็บจำนวนสินค้าในสต็อกของสินค้าที่เลือก
        selected_item_stock_var = tk.StringVar()
        selected_item_stock_label = tk.Label(stock_window, textvariable=selected_item_stock_var, font=("Arial", 18))
        selected_item_stock_label.pack()

        new_stock_label = tk.Label(stock_window, text="จำนวนสินค้าใหม่:", font=("Arial", 18), width=18)
        new_stock_label.pack()
        new_stock_entry = tk.Entry(stock_window, font=("Arial", 18))
        new_stock_entry.pack(pady=10)

    # อัปเดตจำนวนสินค้าในสต็อกเมื่อผู้ใช้เลือกสินค้าในเมนูตัวเลือก
        def update_selected_item_stock():
            selected_item_name = item_var.get()
            selected_item = next((item for item in self.menu if item["food"] == selected_item_name), None)
            if selected_item:
                selected_item_stock_var.set(selected_item["stock"])
            else:
                selected_item_stock_var.set("")
        # การใช้ trace เพื่อติดตามการเปลี่ยนแปลงของ item_var:
        item_var.trace("w", lambda *args, **kwargs: update_selected_item_stock())

        update_stock_button = tk.Button(stock_window, text="อัปเดตสต็อก", command=lambda: self.update_stock(item_var.get(), new_stock_entry.get(), stock_window), font=("Arial", 18), width=12)
        update_stock_button.pack()

        back_to_main_button = tk.Button(stock_window, text="กลับหน้าหลัก", command=stock_window.destroy, font=("Arial", 18), width=12)
        back_to_main_button.pack(pady=10)

         
    # อัปเดตจำนวนสินค้าในสต็อก
    def update_stock(self, item_name, new_stock, window):
        try:
            new_stock_value = int(new_stock)
            if new_stock_value < 0:
                raise ValueError("ค่าสต็อกต้องเป็นจำนวนเต็มบวก")

            # อัปเดตข้อมูลใน SQLite
            self.update_stock_in_database(item_name, new_stock_value)

            # อัปเดตข้อมูลใน self.menu
            self.update_stock_in_menu(item_name, new_stock_value)

            # แสดง messagebox แจ้งเตือนว่าอัปเดตสต็อกสินค้าเสร็จเรียบร้อย
            messagebox.showinfo("สำเร็จ", "อัปเดตสต็อกสินค้าเรียบร้อยแล้ว")

            # อัปเดต GUI ของเลือกสินค้า
            self.update_menu_listbox()
            window.destroy()

        except ValueError as e:
            messagebox.showerror("ข้อผิดพลาด", "กรอกใหม่")

    # เมธอดสำหรับอัปเดต GUI ของเลือกสินค้า
    def update_menu_listbox(self):
        # ลบรายการเก่าใน listbox
        self.cart_listbox.delete(0, tk.END)
        
        # เพิ่มรายการใหม่เข้าไปใน listbox ตามข้อมูลใน self.menu
        for item in self.menu:
            food_name = item["food"]
            stock = item["stock"]
            price = item["price"]
            self.cart_listbox.insert(tk.END, f"{food_name} - ราคา: {price} บาท - สต็อก: {stock}")

    # เพิ่มรายการสินค้าใหม่พร้อมรูปภาพ
    def add_item_with_image(self):
        password_input = simpledialog.askstring("รหัสผ่าน", "กรุณากรอกรหัสผ่าน (4 หลัก):", show="*")
        if  password_input == "1234":
            add_item_window = tk.Toplevel(self.root)
            add_item_window.title("เพิ่มรายการอาหารใหม่")
            add_item_window.geometry("500x500")

            name_label = tk.Label(add_item_window, text="ชื่ออาหาร:", font=("Arial", 14))
            name_label.pack()
            name_entry = tk.Entry(add_item_window, font=("Arial", 14))
            name_entry.pack(pady=10)

            price_label = tk.Label(add_item_window, text="ราคา:", font=("Arial", 14))
            price_label.pack()
            price_entry = tk.Entry(add_item_window, font=("Arial", 14))
            price_entry.pack(pady=10)

            stock_label = tk.Label(add_item_window, text="สต็อก:", font=("Arial", 14))
            stock_label.pack()
            stock_entry = tk.Entry(add_item_window, font=("Arial", 14))
            stock_entry.pack(pady=10)

            animal_label = tk.Label(add_item_window, text="สัตว์เลี้ยง:", font=("Arial", 14))
            animal_label.pack()
            animal_entry = tk.Entry(add_item_window, font=("Arial", 14))
            animal_entry.pack(pady=10)

            browse_button = tk.Button(add_item_window, text="เลือกรูปภาพ", command=lambda: self.browse_image(add_item_window), font=("Arial", 14),width=11)
            browse_button.pack(pady=20)

            save_button = tk.Button(add_item_window, text="บันทึก", command=lambda: self.save_new_item(name_entry.get(), price_entry.get(), stock_entry.get(), animal_entry.get(), add_item_window), font=("Arial", 14), bg="green", fg="white",width=11)
            save_button.pack()

            back_button = tk.Button(add_item_window, text="กลับหน้าหลัก", command=add_item_window.destroy, font=("Arial", 14), bg="red", fg="white",width=11)
            back_button.pack(pady=20)
        else:
            messagebox.showerror("ข้อผิดพลาด", "รหัสผ่านไม่ถูกต้อง")    
    # เพิ่มรูปภาพประสินค้าใหม่
    def browse_image(self, add_item_window):
        file_path = filedialog.askopenfilename(title="เลือกรูปภาพสินค้า")
        if file_path:
            self.new_item_image_path = file_path
            messagebox.showinfo("สำเร็จ", "เลือกรูปภาพสินค้าเรียบร้อยแล้ว")
        else:
            messagebox.showerror("ข้อผิดพลาด", "กรุณาเลือกรูปภาพสินค้า")

    # การบันทึกข้อมูลของสินค้าใหม่
    def save_new_item(self, name, price, stock, animal, add_item_window):
        try:
            price = float(price)
            stock = int(stock)
            if price < 0 or stock < 0:
                raise ValueError("ราคาและสต็อกต้องเป็นค่าที่ไม่ติดลบ")
            if name and animal and self.new_item_image_path:
                # สร้าง dictionary สำหรับรายการสินค้าใหม่
                new_item = {"animal": animal, "food": name, "price": price, "stock": stock, "image": self.load_image(self.new_item_image_path)}
                # เพิ่มรายการสินค้าใหม่ลงในรายการสินค้าของโปรแกรม
                self.menu.append(new_item)
                
                # เก็บรายละเอียดสินค้าใหม่ในฐานข้อมูล SQLite
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO items (name, price, stock, animal) VALUES (?, ?, ?, ?)", (name, price, stock, animal))
                self.conn.commit()
                cursor.close()
                 # ปิดหน้าต่างเพิ่มสินค้าใหม่
                add_item_window.destroy()
                self.destroy_shopping_gui()
                # สร้างหน้า GUI ของหน้าเลือกสินค้าใหม่
                self.create_shopping_gui()
            else:
                messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลให้ครบถ้วนและเลือกรูปภาพสินค้า")
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกราคาและจำนวนสต็อกให้ถูกต้อง")
    
    # สร้างตารางในฐานข้อมูล SQLite สำหรับเก็บข้อมูลการขาย
    def create_sales_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                transaction_id TEXT PRIMARY KEY,
                customer_name TEXT,
                customer_phone TEXT,
                timestamp DATETIME,
                items_details TEXT,
                total_price REAL
            )
        ''')
        self.conn.commit()
    # ฟังก์ชันสร้างตาราง items ใน SQLite
    def create_items_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL,
                animal TEXT NOT NULL,
                image BLOB
            )
        ''')
        self.conn.commit()
        for item in self.menu:
            cursor.execute("INSERT INTO items (name, price, stock, animal) VALUES (?, ?, ?, ?)", (item["food"], item["price"], item["stock"], item["animal"]))
        self.conn.commit()
    # ทำหน้าที่ในการอัปเดตข้อมูลของสินค้าในฐานข้อมูล SQLite โดยใช้ชื่อสินค้า (item_name) และจำนวนสต็อกใหม่ (new_stock) ที่ต้องการอัปเดต.
    def update_stock_in_database(self, item_name, new_stock):
        try:
            # อัปเดตข้อมูลใน SQLite
            cursor = self.conn.cursor()
            cursor.execute("UPDATE items SET stock=? WHERE name=?", (new_stock, item_name))
            self.conn.commit()
            cursor.close()
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการอัปเดตฐานข้อมูล: {str(e)}")


    # ฟังก์ชันที่ใช้ในการอัปเดตสต็อกเมื่อมีการเปลี่ยนแปลงใน self.menu
    def update_stock_in_menu(self, item_name, new_stock):
        # ค้นหาสินค้าใน self.menu และอัปเดตค่าสต็อก
        for item in self.menu:
            if item["food"] == item_name:
                item["stock"] = new_stock
                break      
     
    # ปิดโปรแกรม
    def exit_program(self):
        self.conn.close()
        self.root.destroy()
    # ซ่อนและแสดงหน้าหลักของโปรแกรม
    
    def hide_main_window(self):
        self.welcome_label.pack_forget()
        self.start_shopping_button.pack_forget()
        self.admin_label.pack_forget()
        self.add_item_button.pack_forget()
        self.exit_button.pack_forget()

    # ซ่อนและแสดงหน้าหลักของโปรแกรม
    def show_main_window(self):
        self.welcome_label.pack()
        self.start_shopping_button.pack()
        self.admin_label.pack()
        self.add_item_button.pack()
        self.exit_button.pack()

    # ทำลายหน้า GUI สำหรับการเลือกสินค้าและชำระเงิน
    def destroy_shopping_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # แสดงข้อมูลผู้สร้างในหน้าต่างใหม่
    def show_creator_info(self):
        creators_window = tk.Toplevel(self.root)
        creators_window.title("ข้อมูลผู้สร้าง")
        creators_window.geometry("500x600")
        
    # ข้อมูลผู้สร้าง
        creators_info = [
        {"name": "นายวาทิต คำภักดี", "student_id": "653050154-4", "subject": "วิชาที่เรียน 1", "image_path": "ST1.png"},
        {"name": "นางสาวชนม์พัส พินยะพงค์", "student_id": "653050418-6", "subject": "วิชาที่เรียน 2", "advisor": "", "image_path": "ST2.png"}
    ]

    # แสดงข้อมูลผู้สร้าง
        for creator in creators_info:
            creator_frame = tk.Frame(creators_window, padx=20, pady=20)
            creator_frame.pack(expand=True, fill=tk.BOTH)

            tk.Label(creator_frame, text=f"ชื่อ: {creator['name']}", font=("Arial", 14)).pack()
            tk.Label(creator_frame, text=f"รหัสนักศึกษา: {creator['student_id']}", font=("Arial", 14)).pack()
            
            

        # โหลดภาพผู้สร้าง
            image = self.load_image(creator["image_path"])
            if image:
                image_label = tk.Label(creator_frame, image=image, padx=5)
                image_label.image = image
                image_label.pack()
        back_to_main_button = tk.Button(creators_window, text="กลับหน้าหลัก", command=creators_window.destroy, font=("Arial", 16))
        back_to_main_button.pack(pady=20)
        
    def save_sale_data(self, transaction_id, customer_name, customer_phone, items_details, total_price):
        # บันทึกข้อมูลการขายลงในฐานข้อมูล SQLite
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO sales (transaction_id, customer_name, customer_phone, timestamp, items_details, total_price) VALUES (?, ?, ?, datetime('now', 'localtime'), ?, ?)", (transaction_id, customer_name, customer_phone, items_details, total_price))
        self.conn.commit()
        cursor.close()

    def show_sales_details(self):
        password_input = simpledialog.askstring("รหัสผ่าน", "กรุณากรอกรหัสผ่าน (4 หลัก):", show="*")
        # สร้าง GUI สำหรับแสดงรายละเอียดของการขายรายวัน
        if  password_input == "1234":
            sales_window = tk.Toplevel(self.root)
            sales_window.title("รายละเอียดการขายรายวัน")
            sales_window.geometry("800x700")

        # โหลดข้อมูลการขายจากฐานข้อมูล SQLite
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM sales WHERE date(timestamp) = date('now', 'localtime')")
            sales_data = cursor.fetchall()
            cursor.close()

        # แสดงข้อมูลการขายใน GUI
            sales_listbox = tk.Listbox(sales_window, font=("Arial", 14), width=80, height=20)
            total_sales = 0  # เริ่มต้นค่ายอดรวมทั้งหมดเป็น 0
            for sale in sales_data:
                transaction_info = f"ชื่อลูกค้า: {sale[1]}\nเบอร์โทร: {sale[2]}\nราคารวม: {sale[5]} บาท\n{'*' * 50}"
                sales_listbox.insert(tk.END, transaction_info)
                total_sales += sale[5]  # เพิ่มยอดขายของรายการนี้เข้าไปในยอดรวมทั้งหมด
            sales_listbox.pack(padx=20, pady=20)

            
            total_sales_label = tk.Label(sales_window, text=f"ยอดขายทั้งหมด: {total_sales} บาท", font=("Arial", 16))
            total_sales_label.pack(pady=10)

            back_to_main_button = tk.Button(sales_window, text="กลับหน้าหลัก", command=sales_window.destroy, font=("Arial", 16))
            back_to_main_button.pack(pady=20)
        else:
            messagebox.showerror("ข้อผิดพลาด", "รหัสผ่านไม่ถูกต้อง")     
    def calculate_total_sales(self):
        # คำนวณยอดรวมทั้งหมดของการขายได้จากฐานข้อมูล SQLite
        cursor = self.conn.cursor()
        cursor.execute("SELECT SUM(total_price) FROM sales")
        total_sales = cursor.fetchone()[0]
        cursor.close()
        return total_sales
        
    def edit_customer_gui(self):
        password_input = simpledialog.askstring("รหัสผ่าน", "กรุณากรอกรหัสผ่าน (4 หลัก):", show="*")
        if password_input == "1234":
            edit_window = tk.Toplevel(self.root)
            edit_window.title("Edit Customer Data")
            edit_window.geometry("400x400")

            # แสดงรายชื่อลูกค้าทั้งหมดจาก SQLite
            cursor = self.conn.cursor()
            cursor.execute("SELECT id, name, phone FROM customers")
            customers = cursor.fetchall()
            cursor.close()

            # แสดงรายชื่อลูกค้าในหน้าต่างแก้ไข
            customer_listbox = tk.Listbox(edit_window, font=("Arial", 14), width=40, height=10)
            for customer in customers:
                customer_info = f"ID: {customer[0]}, Name: {customer[1]}, Phone: {customer[2]}"
                customer_listbox.insert(tk.END, customer_info)
            customer_listbox.pack(pady=20)

            # สร้างฟอร์มสำหรับแก้ไขชื่อลูกค้า
            new_name_label = tk.Label(edit_window, text="New Name:")
            new_name_label.pack()
            new_name_entry = tk.Entry(edit_window)
            new_name_entry.pack()

            # ปุ่มสำหรับเรียกใช้ฟังก์ชันแก้ไขชื่อลูกค้า
            edit_button = tk.Button(edit_window, text="Edit", command=lambda: self.edit_selected_customer(new_name_entry.get(), customer_listbox), font=("Arial", 14), width=8)
            edit_button.pack(pady=20)
            back_to_main_button = tk.Button(edit_window, text="กลับหน้าหลัก", command=edit_window.destroy, font=("Arial", 14), width=8)
            back_to_main_button.pack(pady=20)
        else:
            messagebox.showerror("ข้อผิดพลาด", "รหัสผ่านไม่ถูกต้อง")

    def edit_selected_customer(self, new_name, customer_listbox):
        # ดึงข้อมูลลูกค้าที่ถูกเลือกจากรายการลูกค้าทั้งหมด
        selected_customer_info = customer_listbox.get(customer_listbox.curselection())
        selected_customer_id = int(selected_customer_info.split(",")[0].split(":")[1].strip())

        # อัปเดตชื่อลูกค้าใน SQLite
        cursor = self.conn.cursor()
        cursor.execute("UPDATE customers SET name=? WHERE id=?", (new_name, selected_customer_id))
        self.conn.commit()
        cursor.close()

        # แสดงข้อความแจ้งเตือน
        messagebox.showinfo("Success", "Customer name updated successfully.")
      
    
if __name__ == "__main__":
    root = tk.Tk()
    app = PetShopPOS(root)
    root.mainloop()