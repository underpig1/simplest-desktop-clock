@echo off

REM  A very basic clock to get you started

echo COLOR_SHIFT = (0, 0, 0) > "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\custom.py"
echo POSITION = (600, 75) >> "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\custom.py"
echo FONT = ("Ariel", 75, "bold") >> "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\custom.py"
echo INVERSE = 0 >> "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\custom.py"
echo SOLID = 1 >> "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\custom.py"
