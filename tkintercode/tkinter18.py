#list box
from tkinter import *
root=Tk()
lbx=Listbox(selectmode=MULTIPLE)
lbx.pack()
items=["PEN","PENCIL","BOOK","EARSER","SHARPNER"]
for i in items:
    lbx.insert(END,i)
mainloop()