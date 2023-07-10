from tkinter import *


def submit():
    username = entry.get()
    print("Salam " + username)
    
def delete():
    entry.delete(0, END)
    
def backspce():
    entry.delete(len(entry.get())-1, END)


window = Tk()

entry = Entry(window,
              font=("Arial", 40),
              fg="#156bd4",
              bg="#d4a415")
entry.insert(0, 'Введите свой текст:')

entry.pack(side=LEFT)

submit_button = Button(window, text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspce",command=backspce)
backspace_button.pack(side=RIGHT)


window.mainloop()