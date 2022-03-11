import sys
from PyQt5 import QtWidgets
import sqlite3
from PyQt5.QtGui import QFont,QPixmap,QIcon

buttonFont = QFont('Arial', 12)
textFont = QFont('Arial',16)

#!Connect Database
connect = sqlite3.connect('database.db')
cursor = connect.cursor()

class AddPerson(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Person')
        self.setGeometry(150,150,550,550)
        
        titleAddPerson = QtWidgets.QLabel('Add Person',self)
        titleAddPerson.move(215,80)
        titleAddPerson.setFont(textFont)
        picAddPerson = QtWidgets.QLabel(self)
        picAddPerson.setPixmap(QPixmap('add.png'))
        picAddPerson.move(140,55)
        
        self.added_person_firstname = QtWidgets.QLineEdit(self)
        self.added_person_firstname.move(145,135)
        self.added_person_firstname.resize(150,25)
        self.added_person_firstname.setStyleSheet('border:2px solid gray;padding:2px;border-radius:1px;')
        self.added_person_firstname.setPlaceholderText('Input First Name')
        
        self.added_person_lastname = QtWidgets.QLineEdit(self)
        self.added_person_lastname.move(145,170)
        self.added_person_lastname.resize(150,25)
        self.added_person_lastname.setStyleSheet('border:2px solid gray;padding:2px;border-radius:1px;')
        self.added_person_lastname.setPlaceholderText('Input Last Name')
        
        self.added_person_age = QtWidgets.QComboBox(self)
        self.added_person_age.move(145,205)
        self.added_person_age.resize(80,25)
        for i in range(18,101):
            self.added_person_age.addItem(str(i))
        
        
        self.added_person_adress = QtWidgets.QTextEdit(self)
        self.added_person_adress.setStyleSheet('border:2px solid gray;padding:2px;border-radius:1px')
        self.added_person_adress.move(145,240)
        
        addPersonButton = QtWidgets.QPushButton('Add',self)
        addPersonButton.setFont(buttonFont)
        addPersonButton.move(308,440)
        addPersonButton.clicked.connect(self.addPersonFunction)
    
    #!addPersonFunction
    def addPersonFunction(self):
        name = self.added_person_firstname.text()
        surname = self.added_person_lastname.text()
        age = self.added_person_age.currentText()
        adres = self.added_person_adress.toPlainText()
        
        
        if(name and surname and age and adres != ''):
            try:
                cursor.execute('INSERT INTO persons(person_name,person_lastname,age_person,adress_person) VALUES(?,?,?,?)',(name,surname,age,adres))
                connect.commit()
                QtWidgets.QMessageBox.information(self,'Success','User Added Successfully')
                self.added_person_firstname.setText('')
                self.added_person_lastname.setText('')
                self.added_person_age.setCurrentIndex(0)
                self.added_person_adress.setText('')
                
            except:
                QtWidgets.QMessageBox.information(self,'Warning','User Not Added')
        else:
            QtWidgets.QMessageBox.information(self,'Error','Input Data The Field ')
def main():
    app = QtWidgets.QApplication(sys.argv)
    windowmain = AddPerson()
    windowmain.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()