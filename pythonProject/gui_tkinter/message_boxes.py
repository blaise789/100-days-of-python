from tkinter import *
from tkinter import messagebox

window = Tk()


def click():
    # print("you clicked me ")

    # while True:
    #     messagebox.showerror("error", "invalid email")
    if messagebox.askokcancel(title="game exit",message="click ok to exit or cancel to continue"):
        print("you have exited the game successfully")
    else:
        print("you have continued to play you game")
# messagebox=Message()
click_me_butt = Button(window, text="click me", font=("Comic sans", 15), command=click)
click_me_butt.pack()
window.mainloop()
