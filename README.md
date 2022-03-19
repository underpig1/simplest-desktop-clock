# Simplest Desktop Clock

The simplest possible customizable desktop clock on any operating system 😎 made with python

What it does:
- It's a desktop clock
- It changes colors with your wallpaper
The best part is, it's customizable! So have fun!

## Install
To install the program, simply download the project, navigate to the folder, and run `install.bat`.

Then, copy the files to your start folder so it appears every time your computer starts up @ `%appdata%\Microsoft\Windows\Start Menu\Programs\Startup`. You can get to this folder easily by running CTRL + R, pasting the previous path, and pressing run. After you do this, restart your computer and the clock should appear.

To remove the clock, just navigate to the folder and run `uninstall.bat`.

Simple, right?

## Customizing your clock
Run `customize.bat` at any time to customize some properties of the clock, or do it manually by changing values in `custom.py`:
| Property | Description |
| ---- | ---- |
| `COLOR_SHIFT` | RBG values to shift your clock's color from the wallpaper color. Format: `(r, g, b)`. These values can be negative or positive. |
| `POSITION` | Specifies where to place the clock relative to the top right corner of your screen. Format: `(x, y)`. |
| `FONT` | String representing clock text font. |
| `FONT_SIZE` | Integer specifying clock text font size. |
| `FONT_WEIGHT` | String representing clock text font weight (ex. `"bold"`) |
