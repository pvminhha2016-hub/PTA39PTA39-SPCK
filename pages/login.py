from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic

from home import HomeWindow
from singin import SigninWindow


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui", self)

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.open_signin)

    def login(self):
        email = self.email.text()
        password = self.password.text()

        if email and password:
            self.home = HomeWindow()
            self.home.show()
            self.close()
        else:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Vui lòng nhập đầy đủ thông tin!"
            )

    def open_signin(self):
        self.signin = SigninWindow()
        self.signin.show()
        self.close()