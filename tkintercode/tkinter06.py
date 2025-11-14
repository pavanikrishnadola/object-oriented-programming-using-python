#Entry
from tkinter import *
root=Tk()
root.title("Demo Application")
root.geometry("500x300+400+200")
root.config(bg="red")
root.resizable(0,0)
x="Nipuna"
e1=Entry()
e1.pack(pady=20)
e2=Entry()
e2.insert(0,"India")
e2.pack(pady=20)
e3=Entry()
e3.insert(0,x)
e3.pack(pady=20)
mainloop()