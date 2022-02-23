import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

connection = sqlite3.connect("coffe.sqlite")
cur = connection.cursor()


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Эспрессо')
        self.initUi()
        self.pushButton.clicked.connect(self.open_window)
        self.get_info()

    def initUi(self):
        pass

    def get_info(self):
        data = cur.execute(f"""SELECT main.ID, main.specie, main.grade, grind.type,
                               main.taste, main.price, main.volume FROM main
                               JOIN grind ON grind.ID = main.grind""").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Сорт", "Обжарка", "Форма выпуска", 'Вкус', "Цена",
                                                    "Объём"])
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def open_window(self):
        if self.tableWidget.selectedItems():
            self.change_element_window = ChangeElement(self.tableWidget.selectedItems()[0].row())
            self.change_element_window.show()
        else:
            self.add_element_window = AddElement()
            self.add_element_window.show()

    def closeEvent(self, event):
        connection.close()


class ChangeElement(QWidget):
    def __init__(self, id):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.id = id
        self.setWindowTitle('Изменить элемент')
        self.pushBtn.clicked.connect(self.change_element)
        for genre in cur.execute('SELECT type FROM grind'):
            self.comboBox_grind.addItem(genre[0])
        self.insert_data()

    def insert_data(self):
        data = cur.execute(f"""SELECT main.ID, main.specie, main.grade, grind.type,
                               main.taste, main.price, main.volume FROM main
                               JOIN grind ON grind.ID = main.grind""").fetchall()
        data = data[self.id][1:]
        self.lineEdit_specie.setText(data[0])
        self.lineEdit_grade.setText(data[1])
        self.comboBox_grind.setCurrentText(data[2])
        self.lineEdit_taste.setText(data[3])
        self.lineEdit_price.setText(str(data[4]))
        self.lineEdit_volume.setText(str(data[5]))

    def change_element(self):
        try:
            specie = self.lineEdit_specie.text()
            grade = self.lineEdit_grade.text()
            grind = int(cur.execute(f'''SELECT ID FROM grind
                                    WHERE type = "{self.comboBox_grind.currentText()}"'''
                                    ).fetchone()[0])
            taste = self.lineEdit_taste.text()
            price = int(self.lineEdit_price.text())
            volume = int(self.lineEdit_volume.text())
            if price < 0 or volume < 0:
                self.label_error.setText('Неправильно заполнена форма')
                return
        except ValueError:
            self.label_error.setText('Неправильно заполнена форма')
            return
        values = [specie, grade, grind, taste, price, volume, self.id + 1]
        cur.execute(f'''UPDATE main SET specie=?, grade=?, grind=?, taste=?, price=?, volume=? WHERE ID=?''', values)
        connection.commit()
        ex.get_info()
        self.close()


class AddElement(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setWindowTitle('Добавить элемент')
        self.pushBtn.clicked.connect(self.add_element)
        for genre in cur.execute('SELECT type FROM grind'):
            self.comboBox_grind.addItem(genre[0])

    def add_element(self):
        try:
            specie = self.lineEdit_specie.text()
            grade = self.lineEdit_grade.text()
            grind = int(cur.execute(f'''SELECT ID FROM grind
                                    WHERE type = "{self.comboBox_grind.currentText()}"'''
                                    ).fetchone()[0])
            taste = self.lineEdit_taste.text()
            price = int(self.lineEdit_price.text())
            volume = int(self.lineEdit_volume.text())
            if price < 0 or volume < 0:
                self.label_error.setText('Неправильно заполнена форма')
                return
        except ValueError:
            self.label_error.setText('Неправильно заполнена форма')
            return
        values = [specie, grade, grind, taste, price, volume]
        cur.execute(f'''INSERT INTO main(specie, grade, grind, taste, price, volume) VALUES(?,?,?,?,?,?)''', values)
        connection.commit()
        ex.get_info()
        self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
