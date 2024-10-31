from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit

class Login(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.label = QLabel()
        self.backBtn = QPushButton("<-")
        self.chepBtn = QPushButton("로그인")
        self.joinBtn = QPushButton("회원가입")

        # 입력 필드 추가
        self.usernameInput = QLineEdit(self)  # 사용자 이름 입력 필드
        self.usernameInput.setPlaceholderText("사용자 이름을 입력하세요")  # 플레이스홀더 텍스트
        self.passwordInput = QLineEdit(self)  # 비밀번호 입력 필드
        self.passwordInput.setPlaceholderText("비밀번호를 입력하세요")  # 플레이스홀더 텍스트
        self.passwordInput.setEchoMode(QLineEdit.Password)  # 비밀번호 입력 필드는 숨김 처리


        # 버튼 클릭 시 MainWindow의 메서드 호출
        self.backBtn.clicked.connect(self.main_window.go_to_start)
        self.joinBtn.clicked.connect(self.main_window.go_to_join)
        self.chepBtn.clicked.connect(self.main_window.go_to_chep)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.usernameInput)  # 사용자 이름 입력 필드 추가
        layout.addWidget(self.passwordInput)  # 비밀번호 입력 필드 추가
        layout.addWidget(self.backBtn)
        layout.addWidget(self.chepBtn)
        layout.addWidget(self.joinBtn)
        self.setLayout(layout)
