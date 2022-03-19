The simplest possible customizable desktop clock on any operating system 😎 made with python

What it does:
- It's a desktop clock
- It changes colors with your wallpaper

## Install
To install the program, simply download the project, navigate to the folder, and install the requirements:
```
pip install -r requirements.text
```
Customize your clock in `custom.py`. See below for some things you can do to customize it.

Then, copy the files to your start folder so it appears every time your computer starts up @ `%appdata%\Microsoft\Windows\Start Menu\Programs\Startup`. You can get to this folder easily by running CTRL + R, pasting the previous path, and pressing run. After you do this, restart your computer and the clock should appear.

To remove the clock, just delete the files from the start folder and restart your computer.

Simple, right?

## Customizing your clock
Explore some constants in `custom.py`! Here's a quick reference:
| Property | Description |
| ---- | ---- |
| `COLOR_SHIFT` | RBG values to shift your clock's color from the wallpaper color. Format: `(r, g, b)`. These values can be negative or positive. |
| `POSITION` | Specifies where to place the clock relative to the top right corner of your screen. Format: `(x, y)`. |
