import mysql.connector
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("400x200")
conn=mysql.connector.connect(host="localhost",user="root",password="12345",db="demobase",port=3306)
cursor=conn.cursor()
Label(text="Enter Employee Number to delete:",width=30).grid(row=1,column=1)
entry=Text(height=1,width=4,bg="yellow")
entry.grid(row=1,column=2)
def delete_record():
    eno=entry.get("1.0",'end').strip()
    val=int(eno)
    cursor.execute("Delete from myemp where eno=%s",(val,))
    conn.commit()
    if cursor.rowcount>0:
        messagebox.showinfo("success","Employee record is deleted successfully")
    else:
        messagebox.showinfo("Error","Employee not found")
Button(root,text="Delete Record",width=15,bg="red",command=delete_record).grid(row=1,column=4)
root.mainloop()