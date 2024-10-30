from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class OverlayImage(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.overlay_images = ["images/img1.png", "images/img2.png"]  # 오버레이 이미지 목록
        self.current_index = 0
        self.setPixmap(QPixmap(self.overlay_images[self.current_index]))  # 초기 오버레이 이미지 설정
        self.setScaledContents(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 오버레이 이미지 순환
            self.current_index = (self.current_index + 1) % len(self.overlay_images)
            self.setPixmap(QPixmap(self.overlay_images[self.current_index]))
