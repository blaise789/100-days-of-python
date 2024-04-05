from tkinter import *

pills = ["parastmol", "coartem", "pill"]
# para_image=PhotoImage(file="pills2.jpg")
# coar_image=PhotoImage(file="profile.jpg")
# pil_image=PhotoImage(file="prof.jpg")
# all_images=[para_image,
# coar_image,
# pil_image]
# similar to checkbox, but you can only choose one from the group
window = Tk()


def order():
    if x.get() == 0:
        print("you ordered pizza")


x = IntVar()
for index in range(len(pills)):
    radiobutton = Radiobutton(window,
                              text=pills[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=("Impact", 50),
                              # image=all_images[index]
                              indicatoron=False,
                              width=375,
                              command=order
                              )
    # radiobutton.config(bg="#00FF0
    radiobutton.pack(anchor=W)
window.mainloop()
