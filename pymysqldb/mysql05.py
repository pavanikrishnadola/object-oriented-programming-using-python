#updating record
import tkinter as tk
from tkinter import messagebox
import mysql.connector
def fetch_record_from_mysql(eno):
    try:
        conn=mysql.connector.connect(host="localhost",user="root",password="12345",db="demobase",port=3306)
        cursor=conn.cursor()
        cursor.execute("select eno,ename,esal,egarde from myemp where eno=%s",(eno,))
        row=cursor.fetchone()
        conn.close()
        return row
    except mysql.connector.connect.Error as err:
        messagebox.showerror("Database Error",str(err))
        return None
def update_record_in_mysql(old_eno,new_eno,ename,esal,egarde):
    try:
        conn=mysql.connector.connect(host="localhost",user="root",password="12345",db="demobase",port=3306)
        cursor=conn.cursor()
        cursor.execute("UPDATE myemp SET eno=%s, ename=%s, esal=%s, egarde=%s WHERE eno=%s",(new_eno,ename,esal,egarde,old_eno))
        conn.commit()
        affected_rows=cursor.rowcount
        conn.close()
        return affected_rows
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error",str(err))
        return -1
def fetch_record():
    eno=entry_eno.get()
    if not eno:
        messagebox.showwarning("Input error","please enter an employee number")
        return
    row=fetch_record_from_mysql(eno)
    if row:
        entry_eno_new.delete(0,tk.END)
        entry_eno_new.insert(0,row[0])
        entry_ename.delete(0,tk.END)
        entry_ename.insert(0,row[1])
        entry_esal.delete(0,tk.END)
        entry_esal.insert(0,row[2])
        entry_egarde.delete(0,tk.END)
        entry_egarde.insert(0,row[3])
    else:
        messagebox.showinfo("No Record",f"No reecord fonud for employee number{eno}")
def save_update():
    old_eno=entry_eno.get()
    new_eno=entry_eno_new.get()
    ename=entry_ename.get()
    esal=entry_esal.get()
    egarde=entry_egarde.get()
    if not old_eno or not new_eno or not ename or not esal or not egarde:
        messagebox.showwarning("Error","All fields must be filled")
        return
    affected_rows=update_record_in_mysql(old_eno,new_eno,ename,esal,egarde)
    if affected_rows>0:
        messagebox.showinfo("Success",f"Record for employee number {old_eno} has been updated.")
    elif affected_rows==0:
        messagebox.showinfo("No record",f"No record for employee number{old_eno}.")
    else:
        messagebox.showerror("Error",f"An error occured while trying to update the recoed.")
root=tk.Tk()
root.title("Updating Record")
entry_label=tk.Label(root,text="Enter Employee Number to fetch:")
entry_label.pack(pady=5)
entry_eno=tk.Entry(root)
entry_eno.pack(pady=5)
fetch_button=tk.Button(root,text="Fetch the record",command=fetch_record)
label_eno_new=tk.Label(root,text="New employee number:")
label_eno_new.pack(pady=5)
entry_eno_new=tk.Entry(root)
entry_eno_new.pack(pady=5)
label_ename=tk.Label(root,text="Employee Name:")
label_ename.pack(pady=5)
entry_ename=tk.Entry(root)
entry_ename.pack(pady=5)
label_esal=tk.Label(root,text="Employee Salary:")
label_esal.pack(pady=5)
entry_esal=tk.Entry(root)
entry_esal.pack(pady=5)
label_egarde=tk.Label(root,text="Employee Grade:")
label_egarde.pack(pady=5)
entry_egarde=tk.Entry(root)
entry_egarde.pack(pady=5)
save_button=tk.Button(root,text="Save Update",command=save_update)
save_button.pack(pady=10)
root.mainloop()