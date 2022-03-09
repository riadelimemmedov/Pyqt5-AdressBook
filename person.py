#!Person File
import sys
from PyQt5 import QtWidgets
import sqlite3
from PyQt5.QtGui import QFont,QPixmap,QIcon

buttonFont = QFont('Arial', 12)
textFont = QFont('Arial',16)

#!Connect Database
connect = sqlite3.connect('database.db')
cursor = connect.cursor()

class Person(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Person List')
        self.setGeometry(50,50,550,550)
        
        titleTextPerson = QtWidgets.QLabel('Persons',self)
        titleTextPerson.setFont(textFont)
        titleTextPerson.move(210,70)
        
        picPerson = QtWidgets.QLabel(self)
        picPerson.setPixmap(QPixmap('person.png'))
        picPerson.move(150,52)
        
        #!Person List and Fetch Database Data
        self.personList = QtWidgets.QListWidget(self)
        self.personList.move(110,110)
        personsDatabaseDatas = cursor.execute('SELECT * FROM persons')
        for i in personsDatabaseDatas.fetchall():
            self.personList.addItem(str(i[0])+ ') '+i[1]+ ' '+ i[2])

        #!Button CRUD
        personListButton = QtWidgets.QPushButton('Person List',self)
        personListButton.setFont(buttonFont)
        personListButton.setStyleSheet('background-color:#ecf0f1;border:1px solid;border-radius:4px')
        personListButton.resize(150,28)
        personListButton.move(380,110)
        
        addPersonButton = QtWidgets.QPushButton('Add Person',self)
        addPersonButton.setFont(buttonFont)
        addPersonButton.setStyleSheet('background-color:#686de0;border:1px solid;border-radius:4px')
        addPersonButton.resize(150,28)
        addPersonButton.move(380,150)
        
        updatePersonButton = QtWidgets.QPushButton('Update Person',self)
        updatePersonButton.setFont(buttonFont)
        updatePersonButton.setStyleSheet('background-color:#95afc0;border:1px solid;border-radius:4px')
        updatePersonButton.resize(150,28) 
        updatePersonButton.move(380,190)

        delPersonButton = QtWidgets.QPushButton('Delete Person',self)
        delPersonButton.setFont(QFont(buttonFont))
        delPersonButton.setStyleSheet('background-color:#c0392b;border:1px solid;border-radius:4px')
        delPersonButton.resize(150,28)
        delPersonButton.move(380,230)
    
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    personWindow = Person()
    personWindow.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()