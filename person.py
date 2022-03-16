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
        updatePersonButton.clicked.connect(self.updatePerson)

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
    
    #!updatePerson function
    def updatePerson(self):
        self.update_person_data = self.personList.currentItem().text()
        global UpdatedPersonId #global seklinde yazilmasindaki sebeb basqa class icinde istifade olunacag bu deyisken ona gore
        UpdatedPersonId = self.update_person_data.split(')')[0]
        
        #when clicked update person button show UpdatePerson class and close parent Class mean Person clas
        self.update_class = UpdatePerson()
        self.update_class.show()
        self.close()#Person class
        
#?UpdatePerson 
class UpdatePerson(QtWidgets.QWidget):#QtWidgets.QWidget => olmasa pencere acilmaz inheritance yerine bunu yaz
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Updated Person')
        self.setGeometry(50,50,500,500)
        
        try:
            qs = connect.execute('SELECT * FROM persons WHERE person_id=?',(UpdatedPersonId))
            resultdata = qs.fetchall()#fetchall return list, but fetchone return tuple
            
            person_id_database = resultdata[0][0]
            person_name_database = resultdata[0][1]
            person_lastname_database = resultdata[0][2]
            person_age_database = resultdata[0][3]
            person_adress_database = resultdata[0][4]
            
        except:
            print('Error Update User')
    
        update_person_title = QtWidgets.QLabel('Person Update Info',self)
        update_person_title.move(150,40)
        update_person_title.setFont(textFont)

        self.updated_person_name = QtWidgets.QLineEdit(self)
        self.updated_person_name.move(150,85)
        self.updated_person_name.setText(str(person_name_database))
        
        self.updated_person_username = QtWidgets.QLineEdit(self)
        self.updated_person_username.move(150,115)
        self.updated_person_username.setText(str(person_lastname_database))
        
        self.updated_person_age = QtWidgets.QComboBox(self)
        self.updated_person_age.move(150,150)
        self.updated_person_age.resize(80,25)
        for i in range(18,101):
            self.updated_person_age.addItem(str(i))
        self.updated_person_age.setCurrentText(str(person_age_database))
        
            
        self.updated_person_adress = QtWidgets.QTextEdit(self)
        self.updated_person_adress.move(150,185)
        self.updated_person_adress.setText(str(person_adress_database))
        
        self.updated_person_button = QtWidgets.QPushButton('Update',self)
        self.updated_person_button.setFont(buttonFont)
        self.updated_person_button.move(315,382)
        self.updated_person_button.clicked.connect(self.updatepersondatabase)
    
    #!updatepersondatabase function
    def updatepersondatabase(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    personWindow = Person()
    personWindow.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()