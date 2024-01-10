import sys
from PyQt6.QtWidgets import (
    QWidget, 
    QToolTip, 
    QPushButton, 
    QApplication,
    QMessageBox,
    QMainWindow,
    QMenu
    )
from PyQt6.QtGui import (
    QFont,
    QIcon,
    QAction
    )  

class Example(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        

    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(QApplication.instance().quit)


        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.setShortcut('Q')
        qbtn.move(50,50)

        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Joe Mama')
        fileMenu.addAction(exitAct)

        impMenu = QMenu('Hello', self)
        impAct = QAction('World', self)
        impMenu.addAction(impAct)

        newAct = QAction('', self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('Open new window')

        vs = 'View Statusbar'
        viewStatAct = QAction(vs,self,checkable=True)
        viewStatAct.setStatusTip(vs)
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(viewStatAct)

        self.resize(350,250)
        self.center()
        self.setWindowTitle('Window Window')
        self.show()

    def toggleMenu(self,state):

        if state:
            self.statusbar.show()
        else:
            self.statusBar.hide()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                    "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                     QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            
            event.accept()
        else:
            event.ignore()
    
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()