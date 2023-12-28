import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QTableWidgetItem,
                             QMainWindow)


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('git_1/espresso/main.ui', self)
        self.con = sqlite3.connect('git_1/espresso/coffee')
        self.pushButton.clicked.connect(self.select_data)
        self.textEdit.setPlainText('SELECT * FROM coffee')
        # self.select_data()
        
    def select_data(self):
        query = self.textEdit.toPlainText()
        cur = self.con.cursor()
        result = cur.execute(query).fetchall()
        self.tableWidget.setRowCount(len(result))
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
