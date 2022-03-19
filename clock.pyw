import tkinter as tk
from time import sleep, strftime
from PIL import ImageTk, Image, ImageGrab
from colormap import rgb2hex

root = tk.Tk()
root.wm_title("Clock")
root.overrideredirect(True)

COLOR_SHIFT = (-50, -50, -50)

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

def get_accent_color():
    global color
    px = list(ImageGrab.grab().load()[ws - 600, 75])
    for i in range(len(px)):
        shifted = px[i] + COLOR_SHIFT[i]
        if shifted <= 255 and shifted >= 0:
            px[i] = shifted
        elif COLOR_SHIFT[i] > 0:
            px[i] = 255
        else:
            px[i] = 0
    color = rgb2hex(*px)
            

time = tk.StringVar()

get_accent_color()

label = tk.Label(root, textvariable = time, foreground = color, background = "gray", width = 100, height = 110, font = ("Roboto Mono", 75, "bold"))
label.pack(side = "right")

root.geometry('%dx%d+%d+%d' % (500, 110, ws - 600, 75))
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", label["background"])

while True:
    sleep(1)
    tm = strftime('%I:%M')
    time.set(tm if not tm.startswith('0') else tm[1:])
    root.update()
    get_accent_color()
    label.config(foreground = color)
