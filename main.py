import tkinter as tk

from Pages import loading

class MainInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('K9 Vision Control Interface')
        self.setup_window()

        