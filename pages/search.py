from PyQt6.QtWidgets import QWidget, QPushButton, QListView


class SearchPage(QWidget):
    def __init__(self, main):
        super().__init__()

        self.main = main

        self.listView = QListView(self)
        self.listView.setGeometry(200, 50, 500, 400)

        btn_home = QPushButton("Home", self)
        btn_home.setGeometry(20, 20, 100, 40)

        btn_home.clicked.connect(lambda: self.main.stack.setCurrentIndex(0))