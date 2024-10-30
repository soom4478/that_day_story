from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton

class Chepter(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.label = QLabel("꼬리에 꼬리를 무는 이야기들")
        self.backBtn = QPushButton("<-")
        self.chep1 = QPushButton("chep1")

        # 버튼 클릭 시 MainWindow의 메서드 호출
        self.backBtn.clicked.connect(self.main_window.go_to_start)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.backBtn)
        layout.addWidget(self.chep1)
        self.setLayout(layout)
