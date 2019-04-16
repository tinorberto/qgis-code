@echo off
path %PATH%;C:\Program Files\QGIS 3.6\bin
path %PATH%;C:\Program Files\QGIS 3.6\apps\grass\grass76\lib
path %PATH%;C:\Program Files\QGIS 3.6\apps\qt5\bin
path %PATH%;C:\Program Files\QGIS 3.6\apps\qgis\python\qgis\PyQt
path %PATH%;C:\Program Files\QGIS 3.6\apps\Python37\Scripts
set PYTHONPATH=%PYTHONPATH%;C:\Program Files\QGIS 3.6\apps\qgis\python
set PYTHONHOME=C:\Users\pb003357\AppData\Local\Programs\Python\Python36
path %PATH%;C:\Users\pb003357\AppData\Local\Programs\Python\Python36\Scripts

start "VisualCode QGIS" /B "C:\Program Files (x86)\Microsoft VS Code\Code.exe" %*