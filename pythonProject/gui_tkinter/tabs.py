from tkinter import  *
from tkinter import  ttk
# different other widgets
window=Tk()
notebook=ttk.Notebook(window)
# place a notebook on the window
tab1=Frame(notebook)# new frame for tab1
# page
# creates a frames on the notebook
tab2=Frame(notebook)#

# widget that manages the collection of windows and displays
notebook.add(tab1,text="tab1")
# page labels
notebook.add(tab2,text="tab2")
# page labels
notebook.pack(expand=True,fill='both')
Label(tab1,text="hey this is the first page",width=50,height=25).pack()
Label(tab2,text="hey this the second page",width=50,height=25).pack()

window.mainloop()
# label.bind(event,and action response