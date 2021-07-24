import os, sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
    QSizePolicy, QLabel, QFontDialog, QApplication, QFileDialog)
from PyQt5 import QtWidgets
import functions as fc
from tensorflow.keras.models import load_model
import GUI2
import dialog
#from dialog import Ui_Dialog as dialog


class ExampleAppDialog(QtWidgets.QDialog, dialog.Ui_Dialog):
    def __init__(self):      
        super().__init__()
        self.setupUi(self)

class ExampleApp(QtWidgets.QMainWindow, GUI2.Ui_MainWindow):
    
    

    def browse_folder(self):
        self.lineEdit.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            #for file_name in os.listdir(directory):  # для каждого файла в директории
            self.lineEdit.setText(directory)   # добавить файл в listWidget
   
   
    def use(self):
        name0 = self.lineEdit_2.text()
        name1 = self.lineEdit_3.text()
        model=load_model('model12.h5')
        pred = fc.usenet(self.lineEdit.text(), model)
        #fc.rename(self.lineEdit.text(), pred, name0, name1)

    

    
    def __init__(self):       
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.browse_folder)
        self.pushButton_2.clicked.connect(self.use)
        self.dial = ExampleAppDialog()
        self.Learning.clicked.connect(self.dial.exec)###############################################################################

    


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    main_window = ExampleApp()  # Создаём объект класса ExampleApp
    main_window.show()  # Показываем окно
    dial = ExampleAppDialog()
    app.exec_()  # и запускаем приложение
      
    

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()