from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton

class Login(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.label = QLabel("로그인 창")
        self.backBtn = QPushButton("<-")
        self.chepBtn = QPushButton("로그인")
        self.joinBtn = QPushButton("회원가입")

        # 버튼 클릭 시 MainWindow의 메서드 호출
        self.backBtn.clicked.connect(self.main_window.go_to_start)
        self.joinBtn.clicked.connect(self.main_window.go_to_join)
        self.chepBtn.clicked.connect(self.main_window.go_to_chep)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.backBtn)
        layout.addWidget(self.chepBtn)
        layout.addWidget(self.joinBtn)
        self.setLayout(layout)
