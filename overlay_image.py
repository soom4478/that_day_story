from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
class OverlayImage(QLabel):
    def __init__(self, images, parent=None):
        super().__init__(parent)
        self.images = images
        self.current_image = 0
        self.setPixmap(QPixmap(self.images[self.current_image]))

    def change_image(self, index):
        # 두 번째 이미지로 변경
        self.current_image = 1 if self.current_image == 0 else 0
        self.setPixmap(QPixmap(self.images[self.current_image]))
