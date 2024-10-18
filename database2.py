import sqlite3
import csv

connection = sqlite3.connect('mydatabase.db')

connection.execute('''
                CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text NOT NULL,
                age text NOT NULL,
                department text NOT NULL)
                '''
                )
# insert data into table 
employee_data=[
    ("John Doe",32,"Sales"),
    ("Jane Doe",25,"Engineering"),
    ("Fred Doe",45,"Engineering"),
    ("Chris Doe",23,"Sales"),
    ("Layla Doe",35,"Marketing"),
    ("Chalie",25,"HR"),
    ("Samantha",30,"Engineering"),
    ("Sam",27,"Sales"),
    ("Sally",23,"Marketing"),
    ("Mark",40,"Engineering"),
    ("Raj",33,"Engineering")            
]

# connection.executemany('insert  into employees(name, age, department) values(?,?,?)',employee_data)

# query data from database
result=connection.execute("Select * from employees ORDER BY age ASC")
data=result.fetchall()

# display the data
# for row in data:
#     # print('Title: ',row[1])
#     # print('Author: ',row[2])
#     # print('Year: ',row[3])
#     print(f'Name: {row[1]}')
#     print(f'Age: {row[2]}')
#     print(f'Department: {row[3]}',end="\n\n")

# export database table in csv file 
f=open('emp.csv','w')
data=csv.writer(f)
data.writerow(['name','age','department'])
result=connection.execute('select * from employees')
for i in result:
    data.writerow(i)

f.close()   
# matplot lib

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('emp.csv')
data=pd.DataFrame(df)
x=data['name']
y=data['age']
plt.plot(x,y,'o:r')
plt.xlabel('Employees')
plt.ylabel('Age')
plt.legend('FIT LIFE')
plt.title('EMP AGES')
plt.grid(color="black",lw=1,ls='dashdot')
plt.show()






# write the data to the file
connection.commit()

# close the database connection 
connection.close()


