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
        top_frame = LabelFrame(self.root, text="нажми на кнопку")
        bottom_frame = LabelFrame(self.root, text="нажми на вторую кнопку")    
        top_frame.pack(padx=20, pady=30)
        bottom_frame.pack(ipadx=10, ipady=10)
        # self.label.pack(anchor=NW, padx=180, pady=200)
        Label(top_frame, width=30, height=2, bg="#db03fc", text="first").pack(side=LEFT, padx=5, pady=5)
        Label(top_frame, width=30, height=2, bg="#c71e4e", text="second").pack(side=LEFT, padx=5, pady=5)
        Label(bottom_frame, width=30, height=2, bg="#26a1bd", text="free").pack(side=LEFT, padx=5, pady=5)
        Label(bottom_frame, width=30, height=2, bg="#d9c036", text="free").pack(side=LEFT, padx=5, pady=5)



    
    def create_child(self, widht, height, title="Child", resizable=(False, False), icon=None):
        ChildWindow(self.root, widht, height, title, resizable, icon)

if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    # window.create_child(200, 100)
    window.run()
