import tkinter as tk
import threading as tr
import time

win = tk.Tk()
win.attributes("-topmost", True)

t = tk.Label(win, text="FPS")
t.pack()

# ============================

_tick2_frame=0
_tick2_fps=20000000
_tick2_t0=time.time()

def tick(fps=60):
    global _tick2_frame,_tick2_fps,_tick2_t0
    n=_tick2_fps/fps
    _tick2_frame+=n
    while n>0: n-=1:
        if time.time()-_tick2_t0>1:
            _tick2_t0=time.time()
            _tick2_fps=_tick2_frame
            _tick2_frame=0

while True:
    tick(1)
    t["text"]=_tick2_fps

win.mainloop()