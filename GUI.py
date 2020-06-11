from tkinter import *
from main_menu import Main_menu

class GUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("App")
        self.geometry("600x500")
        self.main_menu = Main_menu(self)
        self.main_menu.pack(fill = BOTH, expand = 1)



gui = GUI()

gui.mainloop()