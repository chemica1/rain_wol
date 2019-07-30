import sys
from cx_Freeze import setup, Executable

setup(
    name="MainWindow",
    version="1.0",
    description="wol for huliac",
    author="meoho",
    executables=[Executable("MainWindow.py")])