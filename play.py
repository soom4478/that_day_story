import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSizePolicy, QPushButton, QDialog, QVBoxLayout
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtCore import Qt, QPoint
from overlay_image import OverlayImage

class GameOverDialog(QDialog):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window  # main_window 참조 저장
        self.setWindowTitle("게임 종료")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        label = QLabel("하트가 모두 소진되었습니다. 게임이 종료됩니다.", self)
        layout.addWidget(label)

        ok_button = QPushButton("확인", self)
        ok_button.clicked.connect(self.go_to_story)  # 메서드 연결
        layout.addWidget(ok_button)

        self.setLayout(layout)

    def go_to_story(self):
        self.close()  # 다이얼로그 닫기
        self.main_window.go_to_story()  # story 페이지로 이동

class InfoDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("정보")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        label = QLabel(message, self)
        layout.addWidget(label)

        ok_button = QPushButton("확인", self)
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

        self.setLayout(layout)


class Play(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.하트 = 5  # 하트 변수 초기화

        # QLabel을 사용하여 이미지 로드
        self.image_label = QLabel(self)
        self.pixmap = QPixmap("images/testImg.png")

        self.image_label.setPixmap(self.pixmap)
        self.image_label.setScaledContents(False)
        self.image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.image_label.setFixedSize(self.pixmap.size())
        self.image_label.move(0, 0)

        layout = QVBoxLayout()
        layout.addWidget(self.main_window.statusBar())
        layout.addWidget(self.image_label)
        self.setLayout(layout)

        overlay_positions = [(100, 100), (300, 150), (500, 200), (200, 300), (400, 400)]
        self.overlay_labels = []

        for i, pos in enumerate(overlay_positions):
            overlay_images = [f"images/find_imgs/img{i + 1}.png", f"images/find_imgs/img{i + 1}_2.png"]
            overlay_label = OverlayImage(overlay_images, self)
            overlay_label.setFixedSize(200, 100)
            overlay_label.move(*pos)
            overlay_label.show()
            overlay_label.mousePressEvent = lambda event, idx=i, label=overlay_label: self.handle_overlay_click(event, idx, label)
            self.overlay_labels.append(overlay_label)

        self.image_label.setMouseTracking(True)
        self.image_label.installEventFilter(self)
        for overlay in self.overlay_labels:
            overlay.installEventFilter(self)
        self.last_mouse_pos = None
        self.is_dragging = False  # 드래그 여부 확인 변수
        self.move_limit = 50

    def reset_game(self):
        """게임 상태를 초기화합니다."""
        self.하트 = 5  # 하트 초기화
        self.main_window.statusBar().reset_hearts()  # 상태바의 하트 초기화
        print("게임이 초기화되었습니다.")

    def handle_overlay_click(self, event, index, label):
        if event.button() == Qt.LeftButton:
            label.change_image(index)
            self.show_info_dialog(index)

    def show_info_dialog(self, index):
        dialog_texts = [
            "첫 번째 오버레이 클릭됨",
            "두 번째 오버레이 클릭됨",
            "세 번째 오버레이 클릭됨",
            "네 번째 오버레이 클릭됨",
            "다섯 번째 오버레이 클릭됨"
        ]
        dialog = InfoDialog(dialog_texts[index], self)
        dialog.exec_()

    def eventFilter(self, source, event):
        if source is self.image_label:
            if event.type() == QMouseEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self.last_mouse_pos = event.pos()
                self.is_dragging = False  # 드래그 초기화
                return True
            elif event.type() == QMouseEvent.MouseMove and event.buttons() == Qt.LeftButton:
                if self.last_mouse_pos:
                    delta = event.pos() - self.last_mouse_pos
                    if abs(delta.x()) > 5 or abs(delta.y()) > 5:  # 드래그로 판단하는 기준 (5픽셀 이상 이동 시)
                        self.is_dragging = True
                    delta_x = min(max(delta.x(), -self.move_limit), self.move_limit)
                    delta_y = min(max(delta.y(), -self.move_limit), self.move_limit)
                    new_x = self.image_label.x() + delta_x
                    new_y = self.image_label.y() + delta_y
                    self.image_label.move(new_x, new_y)
                    for overlay in self.overlay_labels:
                        overlay.move(overlay.x() + delta_x, overlay.y() + delta_y)
                    self.last_mouse_pos = event.pos()
                return True
            elif event.type() == QMouseEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                if not self.is_dragging:  # 드래그가 아닌 경우에만 하트 감소
                    click_pos = event.pos()
                    if not any(overlay.geometry().contains(self.mapToGlobal(click_pos)) for overlay in self.overlay_labels):
                        self.하트 -= 1
                        print(f"하트 감소: {self.하트}")
                        self.main_window.statusBar().update_hearts(self.하트)

                        # 하트가 0이 되면 GameOverDialog를 표시
                        if self.하트 <= 0:
                            game_over_dialog = GameOverDialog(self.main_window, self)
                            game_over_dialog.exec_()
                            self.reset_game()  # 게임 상태 초기화

                self.last_mouse_pos = None
                return True
        return super().eventFilter(source, event)
