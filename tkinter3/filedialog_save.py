from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),

                                    ])
    filetext = str(text.get(1.0, END))
    # filetext = input("Введите текст: ")
    file.write(filetext)
    file.close()
    
    
window = Tk()

button = Button(text='save', command=saveFile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()