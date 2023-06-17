# Просмотрщик файлов - Свой мини блокнот

from tkinter import *

def output(event):
    s = ent.get()
    try:
        txt = open(s, "r", encoding="utf-8")
        content = txt.read()
        tex.delete(1.0, END)
        tex.insert(END, content)
    except:
        tex.delete(1.0, END)
        tex.insert(END, "Файл не существует")

root = Tk()
root.title("Блокнот")
root.minsize(width=500, height=400)

ent = Entry(root, width=20)
but = Button(root, text="открыть")
tex = Text(root, width=80, height=30, font="Arial 16", wrap=WORD)

ent.grid(row=0, column=0)
but.grid(row=2, column=0)
tex.grid(row=1, column=0)

but.bind("<Button-1>", output)

root.mainloop()