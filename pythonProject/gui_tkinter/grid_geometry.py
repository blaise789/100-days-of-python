# grid  organizes widgests in a table-like structure
from tkinter import *

window = Tk()
Label(window, text="first Name").grid(row=0, column=0)
Entry(window).grid(row=0, column=1)
Label(window, text="password").grid(row=1, column=0)
Entry(window).grid(row=1, column=1)
Label(window, text="email").grid(row=2, column=0)
Entry(window).grid(row=2, column=1)
Button(window,text="submit").grid(row=3,column=0,columnspan=2)
window.mainloop()
