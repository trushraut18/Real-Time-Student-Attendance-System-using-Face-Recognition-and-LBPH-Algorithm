import os
import csv
import pyodbc 
import pandas as pd
from openpyxl import Workbook
from datetime import datetime

p1=datetime.date(datetime.now())
p=str(datetime.date(datetime.now()))
s=p1.strftime("%B,%Y")

wb = Workbook()
ws = wb.active

if os.path.exists(r'\Reports'+s):
    wb.save(r'\Reports'+s+'report_'+p+'.csv')
else:
    os.mkdir(r'\Reports'+s)
    wb.save(r'\Reports'+s+'report_'+p+'.csv')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TRUSHNA\SQLEXPRESS;'
                      'Database=student_database;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
#cursor for attendance
cursor.execute('SELECT * FROM student_database.dbo.Attendance')
print("attendance data")
for row in cursor:
    print(row)

#cursor1 for attendance
cursor1 = conn.cursor()
cursor1.execute('SELECT * FROM student_database.dbo.Student')
print("student data")
for row1 in cursor1:
    print(row)


sql_query = pd.read_sql_query(''' select * from student_database.dbo.Attendance''',conn)

df = pd.DataFrame(sql_query)

df.to_csv (r'Reports\report_'+p+'.csv', index = True)

