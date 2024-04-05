from tkinter import *

def openFile():
  pass
def saveFile():
    pass
def quit():
    pass
def cut():
    pass
def copy():
    pass
def paste():
    pass

window=Tk()

menubar=Menu(window)
window.config(menu=menubar)
fileMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="file",

                    menu=fileMenu)
fileMenu.add_command(label="Open",
                     # image=openFileIcon
                     # compound='left' to position left relative to the text
                     command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)
# editMenu
editMenu=Menu(menubar,
              # no tearing between our menu and menubar
              tearoff=0,
font=("MV Boli",16)
              )


# label for our menu
menubar.add_cascade(label="Edit",menu=editMenu)
# adds drop down
editMenu.add_command(label="Cut",

                     command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

# add imagees

window.mainloop()