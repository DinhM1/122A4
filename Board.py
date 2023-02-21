from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from Tile import Tile


class Board(QGridLayout):
    def __init__(self, rows=5, cols=5):
        super().__init__()
        self.rows = rows
        self.cols = cols

        for i in range(rows):
            for j in range(cols):
                button = Tile("cyan")
                print(str(i) + str(j))
                button.clicked.connect(self.clicked)
                self.addWidget(button, i, j)

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def clicked(self):
        # print(str(i) + str(j))
        button = self.sender()
        button.set("red")
