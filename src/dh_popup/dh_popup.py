from tkinter import *


class popup(object):

    """
    Really basic override for a popup window that just takes in two strings, width and height and writes the information
    to the popup window.
    """
    root = None

    def __init__(self, title: str, msg: str, width: int, height: int):
        self.top = Toplevel(popup.root)
        self.top.minsize(width, height)
        self.top.maxsize(width, height)
        self.top.title(title)

        heading = Label(self.top, text=msg)
        heading.pack(side=TOP, pady=10)

        button_panel = Frame(self.top)

        ok = Button(button_panel, text="Okay", command=lambda: self.top.destroy())
        ok.pack(side=RIGHT, padx=10)
        button_panel.pack(side=TOP, pady=10)
