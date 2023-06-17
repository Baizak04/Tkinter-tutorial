# Диалоговые окна в Tkinter

from tkinter import *
from tkinter.filedialog import *
import fileinput

root = Tk()
root.title("Пример чего-то")
root.minsize(width=500, height=400)

txt = Text(root, width=40, height=15, font="16")
txt.pack()
op = askopenfilename()

for i in fileinput.input(op):
    txt.insert(END, i)
root.mainloop()

