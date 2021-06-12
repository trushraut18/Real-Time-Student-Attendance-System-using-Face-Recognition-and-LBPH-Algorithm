import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open(r'F:\CollegeProject\Reports\report_2021-06-11.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    next(lines)
    for row in lines:
        x.append(row[1])
        y.append(row[4])
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Attendance Data")
  
plt.xticks(rotation = 25)
plt.xlabel('Date')
plt.ylabel('Number of Students ')
plt.title('Student Attendance Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()



