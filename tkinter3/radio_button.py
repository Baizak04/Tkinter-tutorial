from tkinter import *


food = ["Пицца", "Гамбургер", "Хотдог"]

def order():
    if(x.get()==0):
        print("Вы заказали Пиццу")
    elif(x.get()==1):
        print("Вы заказали Гамбургер")
    elif(x.get()==2):
        print("Вы заказали Хотдог")
    else:
        print("Что?")

window = Tk()

pizzaImage = PhotoImage(file='img/pizza.png')
hamburgerImage = PhotoImage(file='img/hamburger.png')
hotdogImage = PhotoImage(file='img/hotdog.png')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window, 
                               text=food[index], 
                               variable=x, 
                               value=index,
                               padx=15,
                               font=("Poppins", 20),
                               image=foodImages[index],
                               compound='left',
                               indicatoron=0,
                               command=order,
                               width=400
                               )

    radio_button.pack(anchor=W)

window.mainloop()