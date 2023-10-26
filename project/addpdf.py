import sqlite3
from fpdf import FPDF
import subprocess
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
