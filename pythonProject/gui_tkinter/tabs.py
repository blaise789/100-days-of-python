from tkinter import  *
from tkinter import  ttk
# different other widgets
window=Tk()
notebook=ttk.Notebook(window)
frame1=Frame(notebook)# new frame for tab1
frame2=Frame(notebook)#new frame for tab1
# widget that manages the collection of windows and displays
notebook.add(frame1,text="tab1")
# page1
# page2
notebook.add(frame2,text="tab2")
notebook.pack()
window.mainloop()