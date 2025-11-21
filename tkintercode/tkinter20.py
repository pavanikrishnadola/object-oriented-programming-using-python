#message
from tkinter import*
root=Tk()
OurMessage="This is our message"
messageVar=Message(root,text=OurMessage)
messageVar.config(bg="lightgreen")
messageVar.pack()
root.mainloop()