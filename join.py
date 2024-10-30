from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton

class Join(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.label = QLabel("회원가입 창")
        self.backBtn = QPushButton("<-")
        self.loginBtn = QPushButton("로그인")

        # 버튼 클릭 시 MainWindow의 메서드 호출
        self.backBtn.clicked.connect(self.main_window.go_to_start)
        self.loginBtn.clicked.connect(self.main_window.go_to_login)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.backBtn)
        layout.addWidget(self.loginBtn)
        self.setLayout(layout)
