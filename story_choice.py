from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton

class Story(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.label = QLabel("chep1")
        self.backBtn = QPushButton("<-")
        self.story1 = QPushButton("백화점")

        # 버튼 클릭 시 MainWindow의 메서드 호출
        self.backBtn.clicked.connect(self.main_window.go_to_chep)
        self.story1.clicked.connect(self.main_window.go_to_play)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.backBtn)
        layout.addWidget(self.story1)
        self.setLayout(layout)
