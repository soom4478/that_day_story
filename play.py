from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtCore import Qt


class Play(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # QLabel을 사용하여 이미지 로드
        self.image_label = QLabel(self)
        self.pixmap = QPixmap("images/gameImg1.png")  # 이미지 경로를 여기에 설정하세요

        # 이미지 설정
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setScaledContents(False)  # QLabel 크기에 맞게 이미지 스케일을 사용하지 않음
        self.image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # 고정 가능 설정

        # QLabel의 크기를 원본 이미지 크기로 설정
        self.image_label.setFixedSize(self.pixmap.size())  # QLabel의 크기를 원본 이미지 크기로 설정
        self.image_label.move(0, 0)  # QLabel을 기본 위치로 이동

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.main_window.statusBar())
        layout.addWidget(self.image_label)  # 이미지 레이블 추가
        self.setLayout(layout)

        # 특정 위치에 고정된 이미지 레이블 추가
        self.overlay_label = QLabel(self)
        self.overlay_pixmap = QPixmap("images/img1.png")  # 오버레이 이미지 경로를 여기에 설정하세요
        self.overlay_label.setPixmap(self.overlay_pixmap)
        self.overlay_label.setScaledContents(False)  # 오버레이 이미지 스케일을 사용하지 않음
        self.overlay_label.setFixedSize(self.overlay_pixmap.size())  # 오버레이 이미지 크기를 원본 크기로 설정
        self.overlay_position = (100, 100)  # 오버레이 이미지를 배치할 초기 위치
        self.overlay_label.move(*self.overlay_position)  # 오버레이 이미지를 특정 위치에 배치

        # 마우스 이벤트 설정
        self.image_label.setMouseTracking(True)
        self.image_label.installEventFilter(self)  # 마우스 이벤트 필터 설치
        self.last_mouse_pos = None  # 마지막 마우스 위치 초기화
        self.move_limit = 50  # 이동할 수 있는 거리 제한 설정

    # 마우스 이벤트 필터로 드래그 기능 추가
    def eventFilter(self, source, event):
        if source is self.image_label:
            if event.type() == QMouseEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self.last_mouse_pos = event.pos()
                return True
            elif event.type() == QMouseEvent.MouseMove and event.buttons() == Qt.LeftButton:
                if self.last_mouse_pos:
                    delta = event.pos() - self.last_mouse_pos
                    # 이동 거리 제한
                    delta_x = min(max(delta.x(), -self.move_limit), self.move_limit)
                    delta_y = min(max(delta.y(), -self.move_limit), self.move_limit)
                    new_x = self.image_label.x() + delta_x
                    new_y = self.image_label.y() + delta_y
                    self.image_label.move(new_x, new_y)
                    self.overlay_label.move(self.overlay_label.x() + delta_x, self.overlay_label.y() + delta_y)  # 오버레이 이미지 위치 이동
                    self.last_mouse_pos = event.pos()
                return True
            elif event.type() == QMouseEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                self.last_mouse_pos = None
                return True
        return super().eventFilter(source, event)

    # 키 이벤트를 무시하여 스크롤 방지
    def keyPressEvent(self, event):
        event.ignore()
