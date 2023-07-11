from tkinter import *


count = 0

def click():
    global count
    count += 1
    print("Вы нажали", count)
    
window = Tk()

photo = PhotoImage(file='img/AvatarMaker.png')

button = Button(window,
                text="Нажмите меня!",
                command=click,
                font=("Comic Sans", 30),
                fg="#236cd9",
                bg="#2ec21d",
                activeforeground="#2ec21d",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="top")
button.pack()

window.mainloop()