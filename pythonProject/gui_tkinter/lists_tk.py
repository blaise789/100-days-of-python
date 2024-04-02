from tkinter import *
window=Tk()

foods=["Hamburger","Pizza","MilkShake"]
listbox=Listbox(window)
for index  in range(len(foods)):
    listbox.insert(index,foods[index])

listbox.pack()

window.mainloop()