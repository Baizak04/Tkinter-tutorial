from tkinter import *


def submit():
    print("Температура " + str(scale.get()))

window = Tk()

# hotImage = PhotoImage(file='img/fire-min.png')
# hotLabel = Label(image=hotImage)
# hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=('Consolas', 20),
              tickinterval=10,
            #   showvalue=0
            #    resolution=5,
              troughcolor='#10b2e8',
              fg='#e8360e',
              bg='#050505')
scale.set(50)

scale.pack()

button = Button(window, text='submit', command=submit)
button.pack()


window.mainloop()