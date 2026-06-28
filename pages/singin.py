from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic


class SigninWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/register.ui", self)

        self.pushButton.clicked.connect(self.register)

    def register(self):
        email = self.email.text()
        password = self.password.text()

        if email and password:
            QMessageBox.information(
                self,
                "Thông báo",
                "Đăng ký thành công!"
            )
            self.close()
        else:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Vui lòng nhập đầy đủ thông tin!"
            )