from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap

class Chepter(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.backBtn = QPushButton("<-")
        self.label = QLabel("꼬리에 꼬리를 무는 이야기들")
        self.chep1 = QPushButton()

        # 이미지 설정
        pixmap = QPixmap("images/see_image.png")  # 이미지 파일 경로
        self.chep1.setIcon(QIcon(pixmap))
        self.chep1.setIconSize(pixmap.size())  # 아이콘 크기를 이미지 크기로 설정

        # 버튼 클릭 시 MainWindow의 메서드 호출
        self.backBtn.clicked.connect(self.main_window.go_to_start)
        self.chep1.clicked.connect(self.main_window.go_to_story)

        layout = QVBoxLayout()
        layout.setSpacing(80)  # 요소 간의 간격 설정 (원하는 값으로 조정 가능)

        # backBtn의 넓이를 줄이기
        self.backBtn.setFixedWidth(50)  # 원하는 너비로 설정 (50은 예시값)

        # 레이블을 가로로 가운데 정렬하기 위해 QHBoxLayout 추가
        label_layout = QHBoxLayout()
        label_layout.addWidget(self.label)
        label_layout.addStretch()  # 레이블을 가운데로 이동시키기 위한 여백 추가
        label_layout.addStretch()  # 오른쪽 여백 추가

        layout.addWidget(self.backBtn)
        layout.addLayout(label_layout)  # 수평 레이아웃 추가
        layout.addWidget(self.chep1)

        layout.addStretch()  # 아래쪽에 여백 추가

        self.setLayout(layout)

        # 버튼 크기 조정
        self.chep1.setFixedSize(pixmap.size())  # 버튼 크기를 이미지 크기로 설정
