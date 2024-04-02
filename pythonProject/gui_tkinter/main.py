from tkinter import *

# widgets = GUI elements: buttons,textboxes,labels,images
# windows = serves as a container to hold these widgets

window = Tk()
# print(window)
window.geometry("1000x1000")


# window.title("Blaise")
# icon = PhotoImage(file="logo512.png")
# # icon.config(width=20, height=50)
# window.iconphoto(True, icon)
# window.config(background="#5cfcff")
#
# place window on computer screen
# ----------------------------------------------------------------------
# a label= an are widget that holds a text and or an imae within a window
# photo=PhotoImage(file='Capture001.png',)
# # image_types().
# label=Label(window,text="Hello world",font=('Arial',40,'bold'),fg='#00FF00',bg="black",relief=RAISED,bd=10,padx=20,pady=20,image=photo,compound='bottom')
# label.place(x=0,y=100)
# # div
count=0
def greet():
    global  count
    count+=1
    print(count)
like_image=PhotoImage(file="like.png")

button = Button(window, text="hey",
                command=greet, font=('Comic sans', 30),
                fg="grey",
                bg="black",
                # activebackground="grey", activeforeground="black",
                # state=DISABLED,
                image=like_image,
                compound='top',
                padx=80,
                )
button.pack()
window.mainloop()
