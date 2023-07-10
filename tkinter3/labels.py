from tkinter import *

window = Tk()

# photo = PhotoImage(file='img/man.png')

label = Label(window, 
              text="Салам", 
              font=('Arial', 40, 'bold'), 
              fg='#d433a1', 
              bg='black',
              relief=RAISED,
              bd=15,
              padx=25,
              pady=20)
            #   image=photo,
            #   compound='top')
label.pack()
# label.place(x=0, y=0)

window.mainloop()