import cv2
import os
import pyodbc
path = os.path.dirname(os.path.abspath(__file__))

#student database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TRUSHNA\SQLEXPRESS;'
                      'Database=student_database;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
print('\n')
print("Initial table")
print('\n')
cursor.execute('SELECT * FROM student_database.dbo.Student')
data = cursor.fetchall()
print (data)
print('\n')
name=input('Enter Your College Id: ')

full_name = input('Enter Your Full Name: ')

Class = input('Enter Your Class: ')

print('\n')
cursor.execute("""INSERT INTO Student(roll_no, name,class) VALUES (?,?,?)""", (name,full_name,Class))
conn.commit()
#print("Data inserted successfully into student table")
print('\n')

#attendance database
cursor1 = conn.cursor()
#cursor1.execute('SELECT * FROM student_database.dbo.Attendance')

cursor1.execute("""INSERT INTO Attendance(name,roll_no,class) VALUES (?,?,?)""", (full_name,name,Class))
conn.commit()


cursor1.execute('''UPDATE Attendance SET status='Present' where name = (?)''',full_name)
conn.commit()

s = "UPDATE Attendance SET date = getdate();"
cursor1.execute(s)
conn.commit()


cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier(path+r'\Classifiers\face.xml')
i=0
offset=50


while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        i=i+1
        cv2.imwrite(r"dataSet\face-"+name +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.rectangle(im, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.waitKey(100)
    if i>20:
        cam.release()
        cv2.destroyAllWindows()
        break

print("  ")
print("  ")
print("Your Student Data has been Successfully Captured")
print("  ")

