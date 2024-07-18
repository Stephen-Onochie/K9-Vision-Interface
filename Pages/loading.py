from PIL import Image, ImageTk
import tkinter as tk

class LoadingPage(tk.Frame):
    def __init__(self, master):
        super.master = master
        self.load_background()

    def load_background(self):
        #Load and display the background image
        bg_image = Image.open('ADD LINK TO BACKGROUND')
        bg_photo = ImageTk.PhotoImage(bg_image)

        #Make sure the canvas size matches the image size exactly
        self.canvas = tk.Canvas(self, width=bg_width(), height=bg_photo.height())
        self.canvas.pack(fill='both', expand=True)

        