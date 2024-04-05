from tkinter import *
from tkinter import filedialog

window = Tk()

def saveAsFile():
    file=filedialog.asksaveasfile(defaultextension=".txt",filetypes=(("text files",".txt"),("html files",".html"),("all files",  "*.*")))
    print(file)
    if file is None:
        return
    text=text_area.get(1.0,END)

    # text=input("enter your bio")
    file.write(text)
    file.close()
    print(text)

def openfile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\bigirabagaboblaise\\Pictures",title="open you bio files",
                                          filetypes=(("text files","*.txt"),("All files","*.*"))                          )
    print(filepath)
    file=open(filepath, 'r')
    # returns text output
    print(file.read())
    file.close()


button = Button(window, text="open file", command=openfile)
save_button = Button(window, text="save file", command=saveAsFile)
text_area=Text(window)
button.pack()
save_button.place(x=0,y=0)
text_area.pack()
window.mainloop(

)
