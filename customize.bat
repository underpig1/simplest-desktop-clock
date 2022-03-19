@echo off
set /p r="Enter RED value of RGB shift from wallpaper color (value can be negative): "
set /p g="Enter GREEN value of RGB shift from wallpaper color (value can be negative): "
set /p b="Enter BLUE value of RGB shift from wallpaper color (value can be negative): "
set /p x="Enter X value of clock position relative to the top right corner of the screen: "
set /p y="Enter X value of clock position relative to the top right corner of the screen: "
echo COLOR_SHIFT = (%r%, %g%, %b%) > custom.py
echo POSITION = (%x%, %y%) >> custom.py
