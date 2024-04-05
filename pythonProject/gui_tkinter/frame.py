from  tkinter import  *
window=Tk()
frame=Frame(window,bg="red")
frame.pack()
Button(frame,text="W",font=("Consolas",16)).pack(side=TOP)
Button(frame,text="A",font=("Consolas",16)).pack(side=LEFT)
Button(frame,text='S',font=("Consolas",16)).pack(side=LEFT)
Button(frame,text='D',font=("Consolas",16)).pack(side=LEFT)

Button()
window.mainloop()
