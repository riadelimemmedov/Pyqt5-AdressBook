#!Main File
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont,QIcon


buttonFont = QFont('Arial', 12)
textFont = QFont('Arial',16)

class WindowMain(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Adress Book')
        self.setGeometry(50,50,400,400)
        self.setStyleSheet('background-color:#ccffff')
        self.interface()
        
    def interface(self):
        
        #!Person Button
        personButton = QtWidgets.QPushButton('Person List',self)
        personButton.setStyleSheet('background-color:#fff')
        personButton.setFont(QFont(buttonFont))
        personButton.setIcon(QIcon('person.png'))
        personButton.resize(140,30)
        personButton.move(150,50)
        ###################################################################
        
        #!AddPerson Button
        addPersonButton = QtWidgets.QPushButton('Add Person',self)
        addPersonButton.setStyleSheet('background-color:#fff')
        addPersonButton.setFont(QFont(buttonFont))
        addPersonButton.setIcon(QIcon('add.png'))
        addPersonButton.resize(140,30)
        addPersonButton.move(150,100)
        ###################################################################
        aboutButton = QtWidgets.QPushButton('About',self)
        aboutButton.setStyleSheet('background-color:#fff')
        aboutButton.setFont(QFont(buttonFont))
        aboutButton.setIcon(QIcon('about.png'))
        aboutButton.resize(140,30)
        aboutButton.move(150,150)
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    windowmain = WindowMain()
    windowmain.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()