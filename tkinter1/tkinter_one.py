from tkinter import *

def hello(event):
    print("Привет программист!")
root = Tk()
root.title("Программа")
root.geometry("600x300")
but1 = Button(root)
but1["text"] = "нажми"
but1["width"] = 15
but1["height"] = 5
but1.bind("<Button-1>", hello)
but1.pack()

input()