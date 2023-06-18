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
            
        self.label = Label(self.root, text="Click on something", bg="#03b6fc", relief=GROOVE, wraplength=150, font="Raleway 18")
        # self.face_image = PhotoImage(file="img/4.png")
        # self.label = Label(self.root, image=self.face_image)
    def run(self):
        self.draw_widget()
        self.root.mainloop()


    def draw_widget(self):
        self.label.pack(anchor=NW, padx=180, pady=200)

    
    def create_child(self, widht, height, title="Child", resizable=(False, False), icon=None):
        ChildWindow(self.root, widht, height, title, resizable, icon)

if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    # window.create_child(200, 100)
    window.run()
