import os
import tkinter
from tkinter import *
from tkinter import messagebox as mb

root=Tk()

def function1():
    os.system("python dataset_capture.py")
    
def function2():
    os.system("python face_training.py")

def function3():
    os.system("python face_recognition.py")

def function5():
    root.destroy()

def attend():
    os.system("python database.py")
    mb.showinfo('Note', 'Your Attendance Sheet has been generated')

def show():
    os.system("python show-graph.py")

def show_student_db():
    os.system("python show_student_db.py")

def show_attendance_db():
    os.system("python show_attendance_db.py")

def show_absent_students():
    os.system("python show_absent_students.py")

root.configure(background="white")
root.title("FACIAL RECOGNITION BASED ATTENDANCE SYSTEM")


Label(root, text="GOVERNMENT COLLEGE OF ENGINEERING, AMRAVATI",font=("times new roman",30),fg="black",bg="lavender",height=3).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Label(root, text="FACIAL RECOGNITION BASED ATTENDANCE SYSTEM",font=("times new roman",20),fg="black",bg="turquoise3",height=3).grid(row=5,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Create Face Dataset",font=("times new roman",20),bg="VioletRed4",fg='white',command=function1).grid(row=7,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="Train Face Dataset",font=("times new roman",20),bg="black",fg='white',command=function2).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Recognize Face and Set Attendance",font=('times new roman',20),bg="VioletRed4",fg="white",command=function3).grid(row=11,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Generate Attendance Sheet",font=('times new roman',20),bg="black",fg="white",command=attend).grid(row=13,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Show Attendance Graph",font=("times new roman",20),bg="VioletRed4",fg='white',command=show).grid(row=15,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="                 Exit                  ",font=('times new roman',20),bg="red",fg="black",command=function5).grid(row=18,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Show Student Database",font=('times new roman',20),bg="turquoise3",fg="black",command=show_student_db).grid(row=17,columnspan=2,sticky=W+S,padx=5,pady=5)

Button(root,text="Show Attendance Database",font=('times new roman',20),bg="turquoise3",fg="black",command=show_attendance_db).grid(row=17,columnspan=2,padx=5,pady=5)

Button(root,text="Show Absent Students",font=('times new roman',20),bg="turquoise3",fg="black",command=show_absent_students).grid(row=17,columnspan=2,sticky=N+E,padx=5,pady=5)

Label(root, text="Project By - Trushna Raut | Shriya Kulkarni | Mahesh Hatwar | Shubham Waratkar ",font=("times new roman",15),fg="white",bg="black",height=1).grid(row=20,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=2,pady=2)

root.mainloop()