# Import functions getting the verions of QtLibrary and
from PyQt6.QtCore import QT_VERSION_STR 
from PyQt6.QtCore import PYQT_VERSION_STR

# Print the versions of QtLibrary and PyQt6 module
def printVersion():
    print(QT_VERSION_STR)
    print(PYQT_VERSION_STR)

printVersion()

# https://zetcode.com/pyqt6/datetime/