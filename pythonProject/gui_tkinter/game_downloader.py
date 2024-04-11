import time
from tkinter.ttk import *
from tkinter import *


def start():
    game_size = 100
    gb_downloaded = 0
    speed = 1
    print(bar['value'])
    while gb_downloaded < game_size:
        time.sleep(0.5)
        bar['value'] += (speed / game_size) * 100
        gb_downloaded += speed
        percent.set(str(int(gb_downloaded / game_size * 100)) + "%")
        gb_finished.set(str(gb_downloaded)+"/"+str(game_size))
        window.update_idletasks()

    # print(bar.size())


window = Tk()
bar = Progressbar(window, length=300)
bar.pack(pady=30)
percent = StringVar()
gb_finished = StringVar()
Label(window, textvariable=percent).pack()
Label(window, textvariable=gb_finished).pack()
Button(window, text="download", command=start).pack()
window.mainloop()
