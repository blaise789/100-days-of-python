from tkinter import  *
window=Tk()
# photo=PhotoImage(file="",compile())
def submit():
    print("temperature is:",str(scale.get()) +"degrees Celsius")
scale=Scale(window,
            from_=100,
            to=0,
            # orient=HORIZONTAL
            length=500,
            tickinterval=10, # adds a numeric indcators for value
            font=("Consolas",20), # hides  current value
            showvalue=False

            )
scale.set(100)
# it sets the initial position for a person
scale.pack()
button=Button(window,text="submit",command=submit)
button.pack()
window.mainloop()