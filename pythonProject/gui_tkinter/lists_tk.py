from tkinter import *

window = Tk()


def remove():
    for i in reversed(listbox.curselection()):
        print(i)
        print(listbox.get(i))
        listbox.delete(i)

    listbox.config(height=listbox.size())


def add():
    # print(entryBox.get())
    # print(listbox.size())

    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def order():
    try:
        f_selected = []
        for f_sel in listbox.curselection():
            f_selected.append(listbox.get(f_sel))

        # ordered_food = listbox.get(listbox.curselection())
        print("you have ordered: ", end="")
        for food in range(len(f_selected)):
            if food == len(f_selected) - 2:
                print(f_selected[food], end=" and ")
            else:
                print(f_selected[food], end=",")
    except Exception as e:
        print("invalid index ")


foods = ["Hamburger", "Pizza", "MilkShake"]
listbox = Listbox(window, selectmode=MULTIPLE)
listbox.pack()
for index in range(len(foods)):
    listbox.insert(index, foods[index])
listbox.config(height=listbox.size())
order_button = Button(window, text="order", command=order)
order_button.pack()
entryBox = Entry(window)
entryBox.pack()
add_food = Button(window, text="add", command=add)
add_food.pack()
remove_food = Button(window, text="remove", command=remove)
remove_food.pack()
window.mainloop()
