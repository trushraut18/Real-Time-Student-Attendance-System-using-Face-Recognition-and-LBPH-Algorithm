import cv2,os
import numpy as np
from PIL import Image 
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TRUSHNA\SQLEXPRESS;'
                      'Database=student_database;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM student_database.dbo.Student WHERE roll_no = (SELECT MAX(roll_no) FROM student_database.dbo.Student)')
print("newly added entry")
newly_added_name = ''
for row in cursor:
    newly_added_name = row
    print(newly_added_name)
    print(row)
path = os.path.dirname(os.path.abspath(__file__))

recognizer = cv2.face_LBPHFaceRecognizer.create()
recognizer.read(path+r'\trainer\trainer.yml')
faceCascade=cv2.CascadeClassifier(path+r'\Classifiers\face.xml')

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        if(nbr_predicted):
             nbr_predicted=newly_added_name
        else:
            print("unknown")          
        cv2.putText(im,str(nbr_predicted)+"--"+str(conf), (x,y+h),font, 1.1, (0,255,0))
        cv2.imshow('Face Recognizer',im)
        cv2.waitKey(10)
