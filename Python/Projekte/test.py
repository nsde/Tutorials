import tkinter as tk
import threading as tr
from time import sleep

win = tk.Tk()
win.attributes("-topmost", True)

t = tk.Label(win, text="FPS")
t.pack()

frames = 0
print('w1')
while 1:
    frames += 1

def sec(frames):
    print()
    while 1:
        sleep(1)
        t["text"] = frames
        frames = 0

mytr = tr.Thread(target=sec)
mytr.start()

win.mainloop()