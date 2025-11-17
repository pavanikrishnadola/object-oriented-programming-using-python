#calculator
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Demo Application")
root.geometry=("400x200+400+200")
lb1=Label(text="A value")
lb1.grid(row=0,column=0)
tb1=Entry()
tb1.grid(row=0,column=1)
tb1.focus()
lb2=Label(text="B value")
lb2.grid(row=1,column=0)
tb2=Entry()
tb2.grid(row=1,column=1)
tb2.focus()
lb3=Label(text="Result")
lb3.grid(row=2,column=0)
tb3=Entry()
tb3.grid(row=2,column=1)
tb3.focus()
def mysum():
    tb3.delete(0,'end')
    a=int(tb1.get())
    b=int(tb2.get())
    c=a+b
    tb3.insert(0,c)
def mysub():
    tb3.delete(0,'end')
    a=int(tb1.get())
    b=int(tb2.get())
    c=a-b
    tb3.insert(0,c)
def mymul():
    tb3.delete(0,'end')
    a=int(tb1.get())
    b=int(tb2.get())
    c=a*b
    tb3.insert(0,c)
def mydiv():
    try:
        tb3.delete(0,'end')
        a=int(tb1.get())
        b=int(tb2.get())
        c=a/b
        tb3.insert(0,c)
    except:
        tb2.delete(0,'end')
        tb2.focus()
        messagebox.showinfo("Error","Not possible to divide a number with zero")
def myfdiv():
    try:
        tb3.delete(0,'end')
        a=int(tb1.get())
        b=int(tb2.get())
        c=a//b
        tb3.insert(0,c)
    except:
        tb2.delete(0,'end')
        tb2.focus()
        messagebox.showinfo("Error","Not possible to divide a number with zero")
def mymod():
    tb3.delete(0,'end')
    a=int(tb1.get())
    b=int(tb2.get())
    c=a%b
    tb3.insert(0,c)
def myexp():
    tb3.delete(0,'end')
    a=int(tb1.get())
    b=int(tb2.get())
    c=a**b
    tb3.insert(0,c)
def mycf():
    tb1.delete(0,'end')
    tb2.delete(0,'end')
    tb3.delete(0,'end')
    tb1.focus()
def myqf():
    root.quit()
btn1=Button(text="+",width=10,command=mysum)
btn1.grid(row=3,column=0)
btn2=Button(text="-",width=10,command=mysub)
btn2.grid(row=3,column=1)
btn3=Button(text="*",width=10,command=mymul)
btn3.grid(row=3,column=2)
btn4=Button(text="/",width=10,command=mydiv)
btn4.grid(row=4,column=0)
btn5=Button(text="//",width=10,command=myfdiv)
btn5.grid(row=4,column=1)
btn6=Button(text="%",width=10,command=mymod)
btn6.grid(row=4,column=2)
btn7=Button(text="**",width=10,command=myexp)
btn7.grid(row=5,column=0)
btn8=Button(text="<-",width=10,command=mycf)
btn8.grid(row=5,column=1)
btn9=Button(text="X",width=10,command=myqf)
btn9.grid(row=5,column=2)
mainloop()