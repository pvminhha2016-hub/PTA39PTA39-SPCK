from PyQt6.QtWidgets import QMainWindow, QListWidget, QListWidgetItem, QInputDialog
from PyQt6 import uic
from PyQt6.QtCore import Qt
from datetime import datetime


class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # =========================
        # LOAD UI GỐC (KHÔNG SỬA UI)
        # =========================
        uic.loadUi("ui/home.ui", self)

        # =========================
        # TẠO LIST CHI PHÍ BẰNG CODE
        # =========================
        self.list_chi_phi = QListWidget(self)

        # đặt vị trí giống listWidget bên cạnh
        self.list_chi_phi.setGeometry(300, 10, 256, 192)

        # thêm vào giao diện
        self.list_chi_phi.show()

        # =========================
        # CONNECT BUTTON
        # =========================
        self.doanh_thu.clicked.connect(self.add_doanh_thu)
        self.chi_phi.clicked.connect(self.add_chi_phi)

    # =========================
    # LẤY THỜI GIAN
    # =========================
    def get_time(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M")

    # =========================
    # DOANH THU
    # =========================
    def add_doanh_thu(self):
        value, ok = QInputDialog.getText(
            self,
            "Doanh thu",
            "Nhập số tiền thu:"
        )

        if ok and value:
            time = self.get_time()
            text = f"[{time}] Thu: {value} VND"

            self.listWidget.addItem(QListWidgetItem(text))

    # =========================
    # CHI PHÍ
    # =========================
    def add_chi_phi(self):
        value, ok = QInputDialog.getText(
            self,
            "Chi phí",
            "Nhập số tiền chi:"
        )

        if ok and value:
            time = self.get_time()
            text = f"[{time}] Chi: {value} VND"

            self.list_chi_phi.addItem(QListWidgetItem(text))