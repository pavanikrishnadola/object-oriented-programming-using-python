#displaying rows and columns
from tkinter import *
import mysql.connector
root=Tk()
root.geometry("500x300")
my_connect=mysql.connector.connect(host="localhost",user="root",password="12345",db="demobase",port=3306)
my_conn=my_connect.cursor()
my_conn.execute("select* from myemp limit 10")
i=1
for emp in my_conn:
    for j in range(len(emp)):
        e=Entry(width=15,fg="blue")
        e.grid(row=i,column=j)
        e.insert(END,str(emp[j]))
    i+=1
mainloop()