import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtCore import Qt, QPoint


class HiddenObjectGame(QWidget):
    def __init__(self):
        super().__init__()

        # 게임 설정
        self.hidden_object_position = QPoint(200, 150)  # 숨겨진 객체의 위치 (임의의 좌표)
        self.hidden_object_radius = 20  # 숨겨진 객체의 반지름 (클릭 감지 반경)

        # 드래그 기능 설정
        self.dragging = False
        self.drag_offset = QPoint(0, 0)

        # 레이아웃 설정
        self.layout = QVBoxLayout()
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("images/test2.png"))  # 배경 이미지 로드
        self.layout.addWidget(self.image_label)

        self.hidden_object_label = QLabel(self)
        self.hidden_object_label.setPixmap(QPixmap("images/heart.png"))  # 숨겨진 그림 로드
        self.hidden_object_label.move(self.hidden_object_position)  # 숨겨진 그림의 초기 위치 설정
        self.layout.addWidget(self.hidden_object_label)

        self.setLayout(self.layout)
        self.setWindowTitle('숨은 그림 찾기 게임')
        self.setGeometry(100, 100, 800, 600)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            clicked_position = event.pos()
            if self.is_hidden_object_clicked(clicked_position):
                QMessageBox.information(self, "축하합니다!", "숨은 그림을 찾았습니다!")
            else:
                QMessageBox.warning(self, "실패!", "다시 시도해보세요.")

            # 드래그 시작
            self.dragging = True
            self.drag_offset = event.pos() - self.hidden_object_label.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            # 숨겨진 그림을 마우스에 따라 이동
            new_position = event.pos() - self.drag_offset
            self.hidden_object_label.move(new_position)
            self.update()  # UI 업데이트

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = False  # 드래그 종료

    def is_hidden_object_clicked(self, position: QPoint) -> bool:
        # 클릭한 위치와 숨겨진 객체의 거리 계산
        hidden_object_rect = self.hidden_object_label.geometry()
        return hidden_object_rect.contains(position)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = HiddenObjectGame()
    game.show()
    sys.exit(app.exec_())
