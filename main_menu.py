from tkinter import Canvas

class Main_menu(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master)
        self.config(bg = "blue")