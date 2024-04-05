from tkinter import *

# text widget =text area on a window
window = Tk()


def submit():
    input_data = text.get('1.0',END)

    print(input_data)


text = Text(window,bg='gray',font=("Ink free",12))
text.pack()

button = Button(window, text="submit the your bio", font=("Arial", 20), command=submit)
button.pack()
window.mainloop()
