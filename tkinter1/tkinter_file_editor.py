# Программа "Редактор файлов"

from tkinter import *
from tkinter.filedialog import *
import fileinput

def open():
    open_one = askopenfilename()
    print(open_one)
    f = open(open_one, "r", encoding='utf-8')
    content = f.read()
    txt.delete(1.0, END)
    txt.insert(END, content)
    
def save():
    sa = asksaveasfile()
    content = txt.get(1.0, END)
    f = open(sa, "w", encoding="utf-8")
    f.write(content)
    f.close()



root = Tk()
root.title("Текстовый редактор")
root.minsize(width=500, height=400)
m = Menu(root)
root.config(menu=m)

fm = Menu(m)
m.add_cascade(label="Файл", menu=fm)
fm.add_command(label="Открыть...", command=open)
fm.add_command(label="Сохранить как...", command=save)

txt = Text(root, width=40, height=15, font="Arial 14")
txt.pack()

root.mainloop()