from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtCore import Qt
from overlay_image import OverlayImage

class Play(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # QLabel을 사용하여 이미지 로드
        self.image_label = QLabel(self)
        self.pixmap = QPixmap("images/testImg.png")  # 이미지 경로를 여기에 설정하세요

        # 이미지 설정
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setScaledContents(False)
        self.image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.image_label.setFixedSize(self.pixmap.size())
        self.image_label.move(0, 0)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.main_window.statusBar())
        layout.addWidget(self.image_label)
        self.setLayout(layout)

        # OverlayImage 클래스를 사용하여 오버레이 추가
        overlay_images = ["images/img1.png", "images/img2.png"]  # 오버레이 이미지 경로 리스트
        self.overlay_label = OverlayImage(overlay_images, self)
        self.overlay_label.setFixedSize(200, 100)  # 필요에 따라 크기를 조정하세요
        self.overlay_position = (500, 200)
        self.overlay_label.move(*self.overlay_position)

        self.overlay_label2 = OverlayImage(overlay_images, self)
        self.overlay_label2.setFixedSize(200, 100)  # 필요에 따라 크기를 조정하세요
        self.overlay_position2 = (100, 200)
        self.overlay_label2.move(*self.overlay_position2)

        # 마우스 이벤트 설정
        self.image_label.setMouseTracking(True)
        self.image_label.installEventFilter(self)
        self.overlay_label.installEventFilter(self)
        self.overlay_label2.installEventFilter(self)
        self.last_mouse_pos = None
        self.move_limit = 50

    # 마우스 이벤트 필터로 드래그 및 클릭 기능 추가
    def eventFilter(self, source, event):
        if source is self.image_label:
            if event.type() == QMouseEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self.last_mouse_pos = event.pos()
                return True
            elif event.type() == QMouseEvent.MouseMove and event.buttons() == Qt.LeftButton:
                if self.last_mouse_pos:
                    delta = event.pos() - self.last_mouse_pos
                    delta_x = min(max(delta.x(), -self.move_limit), self.move_limit)
                    delta_y = min(max(delta.y(), -self.move_limit), self.move_limit)
                    new_x = self.image_label.x() + delta_x
                    new_y = self.image_label.y() + delta_y
                    self.image_label.move(new_x, new_y)
                    self.overlay_label.move(self.overlay_label.x() + delta_x, self.overlay_label.y() + delta_y)
                    self.overlay_label2.move(self.overlay_label2.x() + delta_x, self.overlay_label2.y() + delta_y)
                    self.last_mouse_pos = event.pos()
                return True
            elif event.type() == QMouseEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                self.last_mouse_pos = None
                return True
        return super().eventFilter(source, event)