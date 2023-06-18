from tkinter import *
from child_window import ChildWindow

class Window:
    def __init__(self, widht, height, title="MyWindow", resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{widht}x{height}+200+200")
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
        f = Frame(self.root)
        f.pack()
        # self.label.pack(anchor=NW, padx=180, pady=200)
        Label(f, width=30, height=2, bg="#db03fc", text="first").pack(side=TOP)
        Label(f, width=30, height=2, bg="#c71e4e", text="second").pack(side=TOP)
        Label(f, width=30, height=2, bg="#26a1bd", text="free").pack(side=BOTTOM)



    
    def create_child(self, widht, height, title="Child", resizable=(False, False), icon=None):
        ChildWindow(self.root, widht, height, title, resizable, icon)

if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    # window.create_child(200, 100)
    window.run()
