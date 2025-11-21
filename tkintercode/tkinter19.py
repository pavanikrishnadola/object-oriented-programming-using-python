from tkinter import *
root = Tk()
lbx = Listbox(selectmode=MULTIPLE)
lbx.pack()
def uilist(event):
    si = lbx.curselection()
    sv = [lbx.get(i) for i in si]
    lb.config(text=f"Selected: {', '.join(sv)}")
items = ["PEN", "PENCIL", "BOOK", "ERASER", "SHARPENER"]
for i in items:
    lbx.insert(END, i)
lbx.bind("<<ListboxSelect>>", uilist)
lb = Label(text="Selected:")
lb.pack()
root.mainloop()
