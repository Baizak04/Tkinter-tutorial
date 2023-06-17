from tkinter import *
from tkinter.filedialog import *
import fileinput
from tkinter.messagebox import *

# открытие файла
def open():
    open_one = askopenfilename()
    print(open_one)
    f = open(open_one, "r", encoding='utf-8')
    content = f.read()
    txt.delete(1.0, END)
    txt.insert(END, content)
# сохранение файла
def save():
    sa = asksaveasfile()
    content = txt.get(1.0, END)
    f = open(sa, "w", encoding="utf-8")
    f.write(content)
    f.close()
# выход из программы
def close_win():
    if askyesno("Выход","Вы уверены?"):
        root.destroy()
        
# вывод справки
def about():
    showinfo("Редактор")


root = Tk()
root.title("Текстовый редактор")
root.minsize(width=500, height=400)
m = Menu(root)
root.config(menu=m)

fm = Menu(m)
m.add_cascade(label="Файл", menu=fm)
fm.add_command(label="Открыть...", command=open)
fm.add_command(label="Сохранить как...", command=save)
fm.add_command(label="Выход", command=close_win)

hm = Menu(m)
m.add_cascade(label="Справка", menu=hm)
hm.add_command(label="О программе", command=about)

txt = Text(root, width=40, height=15, font="Arial 14")
txt.pack()

root.mainloop()