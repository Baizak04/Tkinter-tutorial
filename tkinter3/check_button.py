from tkinter import *


def display():
    if(x.get()==1):
        print("Вы согласны")
    else:
        print("Вы не согласны")

window = Tk()

x = IntVar()

language_programming_photo = PhotoImage(file='img/All.png')

check_button = Checkbutton(window,
                           text="Я согласен с чем-то",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial', 20),
                           fg='#d43515',
                           bg='black',
                           activeforeground='#f2320c',
                           activebackground='black',
                           pady=15,
                           padx=30,
                           image=language_programming_photo,
                           compound='left')


check_button.pack()
window.mainloop()