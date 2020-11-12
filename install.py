from zipfile import ZipFile
from os import system
from elevate import elevate
elevate()

targetdir = "C:/"
filename = "platform-tools.zip"

with ZipFile(filename, "r") as zip:
    zip.extractall(targetdir)

system("path.bat")
