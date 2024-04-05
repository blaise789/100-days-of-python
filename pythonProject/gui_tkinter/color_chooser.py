from tkinter import *
from tkinter import colorchooser  # submodule

window = Tk()
window.geometry("420x420")


def change_bg_color():
    window.config(bg=colorchooser.askcolor() [1])


button = Button(window, text="click me to change the bg color", font=("Comic sans", 15), command=change_bg_color)
button.pack()
window.mainloop()
