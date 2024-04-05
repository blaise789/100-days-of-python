from tkinter import *

window = Tk()


def create_new_window():
    # new_window = Toplevel()
    new_window = Tk()
    # removing the bottom window would affect the top one
    #     Tk() creates an independent window
    window.destroy()


Button(window, text="create a new window", command=create_new_window).pack()
window.mainloop()
