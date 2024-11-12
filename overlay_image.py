from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class OverlayImage(QLabel):
    def __init__(self, image_paths, parent=None):
        super().__init__(parent)
        self.overlay_images = image_paths  # 생성자로 받은 이미지 경로 목록
        self.current_index = 0
        self.setPixmap(QPixmap(self.overlay_images[self.current_index]))  # 초기 오버레이 이미지 설정
        self.setScaledContents(True)
        self.image_changed = False  # 이미지가 한 번만 변경되었는지 여부

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and not self.image_changed:
            # 이미지가 아직 변경되지 않았을 때만 실행
            self.current_index = 1  # 다음 이미지로 변경
            self.setPixmap(QPixmap(self.overlay_images[self.current_index]))
            self.image_changed = True  # 변경된 상태로 표시