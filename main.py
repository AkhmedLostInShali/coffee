import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

connection = sqlite3.connect("coffe.sqlite")
cur = connection.cursor()


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Эспрессо')
        self.initUi()
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

    def closeEvent(self, event):
        connection.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
