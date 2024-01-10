
# Import necessary libraries and modules
import sys
from PyQt6.QtWidgets import QApplication, QWidget

# function decs
def main():

    # Application object creation (required)
    app = QApplication(sys.argv)

    # Widget creation
    w = QWidget() # QWidget like frame. A widget with no parent is a window
    w.resize(250,200)
    w.move(700,500) # Screen placement coords

    w.setWindowTitle('Simple')
    w.show() # Shows widget, since no parent, is window

    sys.exit(app.exec())

if __name__ == '__main__':
    main()