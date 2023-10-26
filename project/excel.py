import sqlite3
import pandas as pd

conn = sqlite3.connect(r"E:\project\databeta.db")

# คิวรีฐานข้อมูล
cursor = conn.cursor()
cursor.execute("SELECT * FROM history")  # แทนที่ 'your_table' ด้วยชื่อตารางของคุณ
data = cursor.fetchall()

columns = [i[0] for i in cursor.description]

# สร้าง DataFrame
df = pd.DataFrame(data, columns=columns)

# เขียน DataFrame เป็นไฟล์ Excel
df.to_excel('datastore.xlsx', index=False)  # แทนที่ 'output.xlsx' ด้วยพาธไฟล์ที่คุณต้องการสร้าง

# ปิดการเชื่อมต่อกับฐานข้อมูล
conn.close()