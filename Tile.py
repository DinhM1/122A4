from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class Tile(QPushButton):
    def __init__(self, color):
        super().__init__("A")
        self.setStyleSheet("background-color : " + color)

    def set(self, color):
        self.setStyleSheet("background-color : " + color)

    def get(self, color):
        return self.color
