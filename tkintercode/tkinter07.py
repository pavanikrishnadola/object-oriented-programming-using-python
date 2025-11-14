#messagebox
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Demo Application")
root.geometry("500x400+400+200")
root.config(bg="cyan")
root.resizable(0,0)
def bgr():
    root.config(bg="red")
    messagebox.showinfo("RED COLOR","You Selected RED")
def bgb():
    root.config(bg="blue")
    messagebox.showinfo("BLUE COLOR","You selected BLUE")
def bgg():
    root.config(bg="green")
    messagebox.showinfo("GREEN COLOR","You Selected GREEN")
def bgy():
    root.config(bg="yellow")
    messagebox.showinfo("YELLOW COLOR","You selected YELLOW")
def bgq():
    root.quit()
    messagebox.showinfo("QUIT","You Are Ready To QUIT")
btn1=Button(text="RED",width=10,command=bgr)
btn1.pack(pady=20)
btn2=Button(text="BLUE",width=10,command=bgb)
btn2.pack(pady=20)
btn3=Button(text="GREEN",width=10,command=bgg)
btn3.pack(pady=20)
btn4=Button(text="YELLOW",width=10,command=bgy)
btn4.pack(pady=20)
btn5=Button(text="QUIT",width=10,command=bgq)
btn5.pack(pady=20)
mainloop()