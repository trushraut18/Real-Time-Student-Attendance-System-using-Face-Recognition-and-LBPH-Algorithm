import pyodbc
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.title("Attendance Database")
my_w.geometry("400x250") 


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TRUSHNA\SQLEXPRESS;'
                      'Database=student_database;'
                      'Trusted_Connection=yes;')


cursor = conn.cursor()
cursor.execute('SELECT * FROM student_database.dbo.Attendance')

e=Label(my_w,width=10,text='Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=0)
e=Label(my_w,width=10,text='Roll No',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=1)
e=Label(my_w,width=10,text='Class',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=2)
e=Label(my_w,width=10,text='Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=3)
e=Label(my_w,width=10,text='Status',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=4)

i=1
for attendance in cursor: 
    for j in range(len(attendance)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, attendance[j])
    i=i+1
my_w.mainloop()