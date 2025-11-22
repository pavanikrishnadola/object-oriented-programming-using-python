import mysql.connector
from tkinter import *
root=Tk()
root.geometry("400x200")
my_connect=mysql.connector.connect(host="localhost",user="root",password="12345",db="demobase",port=3306)
my_cursor=my_connect.cursor()
l1=Label(text="Enter Employee Number:",width=25)
l1.grid(row=1,column=1)
t1=Text(height=1,width=4,bg="yellow")
t1.grid(row=1,column=2)
def my_details():
    eno=t1.get("1.0",'end').strip()
    try:
        val=int(eno)
        query="select *from myemp where eno=%s"
        my_cursor.execute(query,(val,))
        myemp=my_cursor.fetchone()
        if myemp:
            my_str.set("Employee Details:{myemp}")
        else:
            my_str.set("Employee Details not found")
    except ValueError:
        my_str.set("Invalid input. Please enter a valid integer")
btn1=Button(text="Show Details",width=15,bg="red",command=my_details)
btn1.grid(row=1,column=4)
my_str=StringVar()
my_str.set("output")
l2=Label(textvariable=my_str,width=30,fg="red")
l2.grid(row=3,column=1,columnspan=3)
root.mainloop()