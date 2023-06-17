from tkinter import *
root = Tk()
root.title("Изменение цвета окно")

def colorR():
    f1.config(bg="Red")
    
def colorG():
    f1.config(bg="Green")
    
def colorB():
    f1.config(bg="Blue")
    
def square():
    f1.config(width=600)
    f1.config(height=300)
    
def rest():
    f1.config(width=1000)
    f1.config(height=500)

f1 = Frame(root, width=400, height=200, bg="Black")
f1.pack()

m =Menu(root)
root.config(menu=m)

cm= Menu(m)
m.add_cascade(label="Цвет", menu=cm)
cm.add_command(label="красный", command=colorR)
cm.add_command(label="зеленый", command=colorG)
cm.add_command(label="синий", command=colorB)


sm = Menu(m)
m.add_cascade(label="Размер", menu=sm)
sm.add_command(label="500x300", command=square)
sm.add_command(label="900x400", command=rest)


root.mainloop()
