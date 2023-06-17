from logging import root
from tkinter import *

root = Tk()
root.title("пример работы флажков")
root.minsize(width=500, height=400)

var0 = StringVar()
var1 = StringVar()
var2 = StringVar()

ch0 = Checkbutton(root, text="Linux", variable=var0, onvalue="Выбран Linux ", offvalue="-")
ch1 = Checkbutton(root, text="Windows", variable=var1, onvalue="Выбран Windows", offvalue="-")
ch2 = Checkbutton(root, text="Mac Os", variable=var2, onvalue="Выбран Mac Os", offvalue="-")

lis = Listbox(root, height=3)

def result(event):
    v0 = var0.get()
    v1 = var1.get()
    v2 = var2.get()
    l = [v0, v1, v2]
    lis.delete(0,2)
    
    for v in l:
        lis.insert(END, v)
        
but = Button(root, text="Получить значение")
but.bind("<Button-1>", result)

ch0.deselect()
ch1.deselect()
ch2.deselect()

ch0.pack()
ch1.pack()
ch2.pack()
but.pack()
lis.pack()

root.mainloop()