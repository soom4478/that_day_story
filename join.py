from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox
from db_connect import get_connection
from db import insert_user_data

class Join(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.label = QLabel("회원가입")
        self.backBtn = QPushButton("<-")
        self.loginBtn = QPushButton("로그인")
        self.registerBtn = QPushButton("회원가입")  # 새로운 버튼 생성

        # 입력 필드 추가
        self.userIdInput = QLineEdit(self)  # 사용자 이름 입력 필드
        self.userIdInput.setPlaceholderText("사용자 이름을 입력하세요")
        self.passInput = QLineEdit(self)  # 비밀번호 입력 필드
        self.passInput.setPlaceholderText("비밀번호를 입력하세요")
        self.passCheckInput = QLineEdit(self)  # 비밀번호 확인 입력 필드
        self.passCheckInput.setPlaceholderText("비밀번호를 다시 입력하세요")
        self.passInput.setEchoMode(QLineEdit.Password)
        self.passCheckInput.setEchoMode(QLineEdit.Password)

        # 버튼 클릭 시 MainWindow의 메서드 호출
        self.backBtn.clicked.connect(self.main_window.go_to_start)
        self.loginBtn.clicked.connect(self.main_window.go_to_login)
        self.registerBtn.clicked.connect(self.handle_register)  # 버튼 클릭 시 데이터베이스에 삽입하는 함수 연결

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.backBtn)
        layout.addWidget(self.userIdInput)
        layout.addWidget(self.passInput)
        layout.addWidget(self.passCheckInput)
        layout.addWidget(self.registerBtn)  # 새로운 버튼 레이아웃에 추가
        layout.addWidget(self.loginBtn)
        self.setLayout(layout)

    def handle_register(self):
        # 입력 값을 가져오기
        user_id = self.userIdInput.text().strip()
        password = self.passInput.text().strip()
        password_check = self.passCheckInput.text().strip()

        # 비밀번호 확인
        if password != password_check:
            QMessageBox.warning(self, "오류", "비밀번호가 일치하지 않습니다.")
            return

        if user_id and password:
            # `insert_user_data` 함수 호출
            try:
                insert_user_data(user_id, password, 0)
                QMessageBox.information(self, "성공", "회원가입이 완료되었습니다.")
            except Exception as e:
                QMessageBox.critical(self, "오류", f"회원가입 중 오류가 발생했습니다: {str(e)}")
        else:
            QMessageBox.warning(self, "오류", "모든 필드를 입력해 주세요.")
