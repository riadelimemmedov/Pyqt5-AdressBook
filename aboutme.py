#!AboutMe File
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont,QIcon,QPixmap

buttonFont = QFont('Arial', 12)
textFont = QFont('Arial',16)

class AboutMe(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('About Page')
        self.setGeometry(420,80,500,500)
        self.setStyleSheet('background-color:#dcdde1')
        
        self.title = QtWidgets.QLabel('About Program',self)
        self.title.setFont(textFont)
        self.title.setStyleSheet('font-weight: bold;text-align:center;')
        self.title.move(200,45)
        
        self.about_image = QtWidgets.QLabel(self)
        self.about_image.setPixmap(QPixmap('about.png'))
        self.about_image.setStyleSheet('text-align:center;')
        self.about_image.move(125,28)
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    windowmain = AboutMe()
    windowmain.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()