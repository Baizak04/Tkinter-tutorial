from logging import root
from tkinter import *

def exit(event):
    root.destroy()
    
def caption(event):
    t = ent.get()
    lbl.configure(text=t)


root = Tk()
root.title("")
root.minsize(width=500, height=400)

ent = Entry(root, width=100)
lbl = Label(root, width=100)

ent.pack()
lbl.pack()

ent.bind('<Return>', caption)
root.bind('<Control-z>', exit)

root.mainloop()