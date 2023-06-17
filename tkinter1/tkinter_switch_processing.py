# обработка переключетелей в Tkinter 
from tkinter import *

def sel():
    selection = "вы выбрали" + str(var.get())
    label.config(text = selection)

root = Tk()
root.title("Пример работы радио кнопок")
root.minsize(width=500, height=400)

var = IntVar()

R1 = Radiobutton(root, text="Linux", variable=var, value=1, command=sel)
R2 = Radiobutton(root, text="Mac Os", variable=var, value=2, command=sel)
R3 = Radiobutton(root, text="Windows", variable=var, value=3, command=sel)

R1.pack(anchor= W)
R2.pack(anchor= W)
R3.pack(anchor= W)

label = Label(root)
label.pack()




root.mainloop()