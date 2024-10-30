from PyQt5.QtWidgets import QStatusBar, QLabel
from PyQt5.QtGui import QPixmap


class CustomStatusBar(QStatusBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 상태바 스타일 설정 (배경색 및 텍스트 색상)
        self.setStyleSheet("background-color: white; color: white;")

        # 상태바에 이미지 추가
        self.heart_img1 = QLabel()
        self.heart_img1.setPixmap(QPixmap("images/heart.png"))

        self.heart_img2 = QLabel()
        self.heart_img2.setPixmap(QPixmap("images/heart.png"))

        self.heart_img3 = QLabel()
        self.heart_img3.setPixmap(QPixmap("images/heart.png"))

        self.heart_img4 = QLabel()
        self.heart_img4.setPixmap(QPixmap("images/heart.png"))

        self.heart_img5 = QLabel()
        self.heart_img5.setPixmap(QPixmap("images/heart.png"))

        self.addPermanentWidget(self.heart_img1)
        self.addPermanentWidget(self.heart_img2)
        self.addPermanentWidget(self.heart_img3)
        self.addPermanentWidget(self.heart_img4)
        self.addPermanentWidget(self.heart_img5)

