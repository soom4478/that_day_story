import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSizePolicy, QPushButton, QDialog
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtCore import Qt
from overlay_image import OverlayImage

class ClearDialog(QDialog):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window  # main_window 참조 저장
        self.setWindowTitle("게임 클리어")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        label = QLabel("모든 원인과 전조증상을 발견하였습니다! \n 삼풍백화점이 붕괴되었습니다.", self)
        layout.addWidget(label)

        ok_button = QPushButton("확인", self)
        ok_button.clicked.connect(self.go_to_story)
        layout.addWidget(ok_button)

        self.setLayout(layout)

    def go_to_story(self):
        self.close()
        self.main_window.go_to_story()

class GameOverDialog(QDialog):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window  # main_window 참조 저장
        self.setWindowTitle("게임 종료")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        label = QLabel("하트가 모두 소진되었습니다. \n 이전 화면으로 돌아갑니다.", self)
        layout.addWidget(label)

        ok_button = QPushButton("확인", self)
        ok_button.clicked.connect(self.go_to_story)  # 메서드 연결
        layout.addWidget(ok_button)

        self.setLayout(layout)

    def go_to_story(self):
        self.close()
        self.main_window.go_to_story()

class InfoDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("원인과 전조증상")
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
        self.heart = 5  # 하트 변수 초기화
        self.changed_overlays = set()  # 이미지가 변경된 오버레이 인덱스를 추적하는 집합

        self.image_label = QLabel(self)
        self.pixmap = QPixmap("images/gmaeImg.png") # 배경

        self.image_label.setPixmap(self.pixmap)
        self.image_label.setScaledContents(False)
        self.image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.image_label.setFixedSize(self.pixmap.size())
        self.image_label.move(0, 0)

        layout = QVBoxLayout()
        layout.addWidget(self.main_window.statusBar())
        layout.addWidget(self.image_label)
        self.setLayout(layout)

        overlay_positions = [(410, 80), (651, 580), (722, 1240), (357, 1450), (942, 1420)]
        self.overlay_labels = []

        for i, pos in enumerate(overlay_positions):
            overlay_images = [f"images/find_imgs/img{i + 1}.png", f"images/find_imgs/img{i + 1}_2.png"]
            overlay_label = OverlayImage(overlay_images, self)
            overlay_label.setFixedSize(235, 218)
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

    def handle_overlay_click(self, event, index, label):
        if event.button() == Qt.LeftButton:
            label.change_image(index)
            self.changed_overlays.add(index)
            self.show_info_dialog(index)

            # 모든 이미지가 변경되었는지
            if len(self.changed_overlays) == len(self.overlay_labels):
                self.show_clear_dialog()

    def show_clear_dialog(self):
        clear_dialog = ClearDialog(self.main_window, self)
        clear_dialog.exec_()

    def reset_game(self): # 게임 초기화함
        self.heart = 5  # 하트 초기화
        self.main_window.statusBar().reset_hearts()  # 상태바의 하트 초기화

    def show_info_dialog(self, index):
        dialog_texts = [
            "바퀴로 옮긴 환풍구",
            "부실공사",
            "식당가에 나타난 싱크홀",
            "붕괴 전 울린 소음",
            "아무 대응 않는 관계자들"
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
                        self.heart -= 1
                        print(f"하트 감소: {self.heart}")
                        self.main_window.statusBar().update_hearts(self.heart)

                        # 하트가 0이 되면 GameOverDialog를 표시
                        if self.heart <= 0:
                            game_over_dialog = GameOverDialog(self.main_window, self)
                            game_over_dialog.exec_()
                            self.reset_game()  # 게임 상태 초기화

                self.last_mouse_pos = None
                return True
        return super().eventFilter(source, event)
