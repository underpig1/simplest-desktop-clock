pip install -r requirements.txt
xcopy clock.pyw "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\"
xcopy custom.py "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\"
"%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\clock.pyw"
