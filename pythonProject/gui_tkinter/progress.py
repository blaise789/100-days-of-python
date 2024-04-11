import time
from tkinter.ttk import *
from tkinter import *


def start():
    tasks = 10
    i = 0
    while (i<tasks):
        time.sleep(1)
        bar['value'] +=10

        i += 1
        percent.set(str(int((i / tasks) * 100)) + "%")
        task_completed.set(str(i)+"/"+str(tasks)+" completed")
        window.update_idletasks()


window = Tk()
bar = Progressbar(window, length=300)
bar.pack(pady=30)
percent = StringVar()
task_completed=StringVar()
Label(window, textvariable=percent).pack()
Label(window,textvariable=task_completed).pack()
Button(window, text="download", command=start).pack()

window.mainloop()
