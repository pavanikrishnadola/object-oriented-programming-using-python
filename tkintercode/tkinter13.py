#Checkbutton code 2
from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Checkbutton")
def update_label():
    selected=[text for var,text in zip(vars,texts)if var.get()==1]
    label.config(text=",".join(selected))
vars=[]
texts=["DCA","PGDCA","PYTHON"]
for text in texts:
    var=IntVar()
    vars.append(var)
    checkbox=Checkbutton(text=text,variable=var,command=update_label)
    checkbox.pack(anchor='w')
    label=Label(text="")
    label.pack()
root.mainloop()