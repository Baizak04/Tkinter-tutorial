from tkinter import *


class Window:
    def __init__(self, widht, height, title="MyWindow", resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{widht}x{height}+200+200")
        self.root.resizable([0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)
            
    
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    window.run()
