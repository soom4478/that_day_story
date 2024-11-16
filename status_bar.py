from PyQt5.QtWidgets import QStatusBar, QLabel
from PyQt5.QtGui import QPixmap

class CustomStatusBar(QStatusBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 상태바 스타일 설정 (배경색 및 텍스트 색상)
        self.setStyleSheet("background-color: white; color: white;")
        self.setFixedHeight(70)  # 원하는 높이 값으로 변경

        # 상태바에 하트 이미지 추가
        self.heart_images = []
        for _ in range(5):
            heart_label = QLabel()
            heart_label.setPixmap(QPixmap("images/heart.png"))
            self.addPermanentWidget(heart_label)
            self.heart_images.append(heart_label)

    def update_hearts(self, remaining_hearts):
        for i in range(5):
            if i < remaining_hearts:
                # 남아있는 하트는 기본 이미지 유지
                self.heart_images[i].setPixmap(QPixmap("images/heart.png"))
            else:
                # 소진된 하트는 다른 이미지로 변경
                self.heart_images[i].setPixmap(QPixmap("images/empty_heart.png"))

    def reset_hearts(self):
        # 모든 하트 이미지를 기본 상태로 복원
        for heart_label in self.heart_images:
            heart_label.setPixmap(QPixmap("images/heart.png"))
