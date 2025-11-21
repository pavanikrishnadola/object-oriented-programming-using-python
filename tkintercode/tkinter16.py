#combo box
from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Combo box Ex")
combobox=ttk.Combobox()
combobox['values']=("PEN","PENCIL","BOOK")
combobox.current(0)
combobox.pack()
mainloop()