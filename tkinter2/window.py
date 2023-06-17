from tkinter import *
from child_window import ChildWindow

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

    
    def create_child(self, widht, height, title="Child", resizable=(False, False), icon=None):
        ChildWindow(self.root, widht, height, title, resizable, icon)

if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    window.create_child(200, 100)
    window.run()
