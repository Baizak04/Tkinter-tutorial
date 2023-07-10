from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Программа с графическим интерфейсом")

icon = PhotoImage(file='img/icon.png')
window.iconphoto(True, icon)
window.config(background="#9333d4")

window.mainloop()
