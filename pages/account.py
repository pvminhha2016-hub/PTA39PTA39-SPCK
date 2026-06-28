from PyQt6.QtWidgets import QWidget, QPushButton, QLabel


class AccountPage(QWidget):
    def __init__(self, main):
        super().__init__()

        self.main = main

        self.label = QLabel("ACCOUNT PAGE", self)
        self.label.setGeometry(200, 50, 200, 50)

        btn_home = QPushButton("Home", self)
        btn_home.setGeometry(20, 20, 100, 40)

        btn_home.clicked.connect(lambda: self.main.stack.setCurrentIndex(0))