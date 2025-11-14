#Styling
from tkinter import *
root=Tk()
root.title("Demo Application")
root.geometry("500x300+400+200")
root.config(bg="red")
root.resizable(0,0)
lb1=Label(text="Tkinter Application",bg="lightgreen",fg="blue",font=("verdana",20,"bold","italic","underline"))
lb1.pack(pady=20)
mainloop()