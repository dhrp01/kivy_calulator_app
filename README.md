#CALCULATOR APP USING KIVY
Its a basic calculator program written using python, kivy. Executable file for windows was built using pyinstaller. Android apk was built using buildozer.

###Kivy
For installing kivy on windows: https://kivy.org/doc/stable/installation/installation-windows.html#install-win-dist

For linux run: `python -m pip install kivy`

###PACKAGING FOR WINDOWS
For packaging in windows, use pyinstaller. Windows client needed.

`pip install pyinstaller`

Use following command to package as windows executable file

`pyinstaller main.py -w --onefile`

###PACKAGING FOR ANDROID
For packaging for android used buildozer. One will also require linux client.

`pip install buildozer`

Create new folder and run `buildozer init`. A buildozer.spec is created, edit it according to the need.

After installing dependencies for buildozer, copy the .py file to the created folder and rename it to main.py. Now run

`buildozer -v android debug`

Takes some time to build and after it does copy apk to mobile and install it. All set now...  