import tkinter as tk
from time import sleep, strftime
from PIL import ImageTk, Image, ImageGrab
from colormap import rgb2hex
from custom import COLOR_SHIFT, POSITION, FONT, INVERSE, SOLID

root = tk.Tk()
root.wm_title("Clock")
root.overrideredirect(True)

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

def get_accent_color():
    global color
    if SOLID != 1:
        try:
            px = list(ImageGrab.grab().load()[ws - POSITION[0], POSITION[1]])
        except:
            px = (0, 0, 0)
        for i in range(len(px)):
            if INVERSE == 1:
                px[i] = 255 - px[i]
            shifted = px[i] + COLOR_SHIFT[i]
            if shifted <= 255 and shifted >= 0:
                px[i] = shifted
            elif COLOR_SHIFT[i] > 0:
                px[i] = 255
            else:
                px[i] = 0
    else:
        px = COLOR_SHIFT
    color = rgb2hex(*px)
            

time = tk.StringVar()

get_accent_color()

label = tk.Label(root, textvariable = time, foreground = color, background = "gray", width = 100, height = 110, font = FONT)
label.pack(side = "right")

root.geometry('%dx%d+%d+%d' % (500, 110, ws - POSITION[0], POSITION[1]))
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", label["background"])

while True:
    sleep(1)
    tm = strftime('%I:%M')
    time.set(tm if not tm.startswith('0') else tm[1:])
    root.update()
    get_accent_color()
    label.config(foreground = color)
