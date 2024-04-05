from tkinter import *

window = Tk()


#
#
# def handleSubmit():
#     username = entry.get()
#     entry.config(state=DISABLED)
#     print(username)
# def delete_user_input():
#     entry.delete(0,END)
# def back_space():
#     entry.delete(len(entry.get())-1,END)
#
#
# entry = Entry(window, font=('Comic sans', 30),show=".")
# entry.pack(side=LEFT)
# backspace = Button(window,text="backspace", font=('Comic sans', 20), command=back_space)
# backspace.pack(side=RIGHT)
# delete_button = Button(window,text="delete", font=('Comic sans', 20), command=delete_user_input)
# delete_button.pack(side=RIGHT)
# button = Button(window,text="submit", font=('Comic sans', 20), command=handleSubmit)
# button.pack(side=RIGHT)
def display():
    if x.get():
        print("you agree")
    else:
        print("you disagree")


x = BooleanVar()
like_photo = PhotoImage(file="like.png")
check_button = Checkbutton(window, text="I agree the terms above", variable=x, onvalue=True, offvalue=False,
                           command=display, bg="black", fg="#00FF00", font=('Arial', 16), activebackground="black",
                           activeforeground="#00FF00", image=like_photo, compound=LEFT)

check_button.pack()
window.mainloop()
