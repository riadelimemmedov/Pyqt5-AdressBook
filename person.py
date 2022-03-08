#!Person File
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont,QPixmap,QIcon

buttonFont = QFont('Arial', 12)
textFont = QFont('Arial',16)

class Person(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Person List')
        self.setGeometry(50,50,500,500)
        
        titleTextPerson = QtWidgets.QLabel('Persons',self)
        titleTextPerson.setFont(textFont)
        titleTextPerson.move(210,70)
        
        picPerson = QtWidgets.QLabel(self)
        picPerson.setPixmap(QPixmap('person.png'))
        picPerson.move(100,40)
        
        self.personList = QtWidgets.QListWidget(self)
        self.personList.move(110,100)

        addPersonButton = QtWidgets.QPushButton('Add Person',self)
        addPersonButton.setFont(buttonFont)
        addPersonButton.move(380,100)
        
        updatePersonButton = QtWidgets.QPushButton('Update Person',self)
        updatePersonButton.setFont(buttonFont)
        updatePersonButton.move(380,140)


def main():
    app = QtWidgets.QApplication(sys.argv)
    personWindow = Person()
    personWindow.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()