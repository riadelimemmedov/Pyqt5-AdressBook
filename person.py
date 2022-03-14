#!Person File
import sys
from PyQt5 import QtWidgets
import sqlite3
import addperson
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
        self.setGeometry(100,100,550,550)
        
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

        #!Button CRUD Button
        
        #?PersonList Button
        personListButton = QtWidgets.QPushButton('Person List',self)
        personListButton.setFont(buttonFont)
        personListButton.setStyleSheet('background-color:#ecf0f1;border:1px solid;border-radius:4px')
        personListButton.resize(150,28)
        personListButton.move(380,110)
        
        #?AddPerson Button
        addPersonButton = QtWidgets.QPushButton('Add Person',self)
        addPersonButton.setFont(buttonFont)
        addPersonButton.setStyleSheet('background-color:#686de0;border:1px solid;border-radius:4px')
        addPersonButton.resize(150,28)
        addPersonButton.move(380,150)
        addPersonButton.clicked.connect(self.addPersonFunc)
        
        #?UpdatePerson Button
        updatePersonButton = QtWidgets.QPushButton('Update Person',self)
        updatePersonButton.setFont(buttonFont)
        updatePersonButton.setStyleSheet('background-color:#95afc0;border:1px solid;border-radius:4px')
        updatePersonButton.resize(150,28) 
        updatePersonButton.move(380,190)

        #?DeletePerson Button
        delPersonButton = QtWidgets.QPushButton('Delete Person',self)
        delPersonButton.setFont(QFont(buttonFont))
        delPersonButton.setStyleSheet('background-color:#c0392b;border:1px solid;border-radius:4px')
        delPersonButton.resize(150,28)
        delPersonButton.move(380,230)
        delPersonButton.clicked.connect(self.deletePersonFunc)
        
    #!addPersonFunc function
    def addPersonFunc(self):
        self.add_person_data = addperson.AddPerson()
        self.add_person_data.show()#Yeni AddPerson penceresini ac
        self.close()#Oldugumu penecereni bagla oldugum pencere ele self dir
        
    #!deletePersonFunc function
    def deletePersonFunc(self):
        self.delete_person_data = self.personList.currentItem().text()
        DeletedPersonId = self.delete_person_data.split(')')[0]
        allowDeleted = QtWidgets.QMessageBox.question(self,'Alert','Are you sure you want to delete the user?',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)

        if(allowDeleted == QtWidgets.QMessageBox.Yes):#yeni yes secdimse sil default onsuzda QtWidgets.QMessageBox.No vermisem 3 cu parametre olarag
            #error handling with => try anc except in python
            try:
                cursor.execute(f'DELETE FROM persons WHERE person_id={DeletedPersonId}')
                #ve ya
                #cursor.execute('DELETE FROM persons WHERE person_id=?',(DeletedPersonId))
                connect.commit()
                QtWidgets.QMessageBox.information(self,'Info','Person Deleted')
            except:
                QtWidgets.QMessageBox.information(self,'Error','Person Not Deleted')
                print('Hata Olustu')
            
            #after deleted person close window
            #self = Person class
            self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    personWindow = Person()
    personWindow.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()