from tkinter import *

root = Tk()
root.title("Программа")      # Заголовок окна
root.geometry("800x400")     # начальные размеры окна

# but = Button(root,
#              text="нажми",
#              width=20, height=2,
#              bg="white", fg="blue")

# lab = Label(root, text="что-то", font="Arial 16")

# ent = Entry(root, width=15, bd=2)

# text = Text(root, width=15, font="Oswald 16", wrap=WORD)

# var = IntVar()

# var.set(1)
# r1 = Radiobutton(root, text="Windows", variable=var, value=0)
# r2 = Radiobutton(root, text="Linux", variable=var, value=1)

# c1 = IntVar()
# c2 = IntVar()

# che1 = Checkbutton(root, text="первый флажок", variable=c1, offvalue=0)
# che2 = Checkbutton(root, text="второй флажок", variable=c2, offvalue=0)


# # but.pack()
# # ent.pack()
# # lab.pack()
# # text.pack()
# r1.pack()
# r2.pack()
# che1.pack()
# che2.pack()

r = ['Python', 'C#', 'C++', 'java', 'C+']
lis = Listbox(root, selectmode=SINGLE, height=5)
for i in r:
    lis.insert(END, i)
    
lis.pack()
root.mainloop()