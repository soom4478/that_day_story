import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from start import Start
from login import Login
from join import Join
from chepter_choice import Chepter
from play import Play
from status_bar import CustomStatusBar  # 커스텀 상태바 불러오기

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("그날이야기")
        self.setFixedSize(1600, 900)  # 고정 크기 설정

        # QStackedWidget 생성 및 설정
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # 페이지 인스턴스 생성 및 QStackedWidget에 추가
        self.start = Start(self)
        self.login = Login(self)
        self.join = Join(self)
        self.chep = Chepter(self)
        self.play = Play(self)  # Play 인스턴스 생성
        self.stacked_widget.addWidget(self.start)
        self.stacked_widget.addWidget(self.login)
        self.stacked_widget.addWidget(self.join)
        self.stacked_widget.addWidget(self.chep)
        self.stacked_widget.addWidget(self.play)

        # 커스텀 상태바 설정
        self.status_bar = CustomStatusBar(self)
        self.setStatusBar(self.status_bar)
        self.status_bar.hide()  # 기본적으로 상태바 숨기기

        # 초기 화면을 start로 설정
        self.stacked_widget.setCurrentWidget(self.start)

    # 페이지 전환 메서드들 정의
    def go_to_login(self):
        self.stacked_widget.setCurrentWidget(self.login)
        self.status_bar.hide()  # login에서는 상태바 숨기기

    def go_to_start(self):
        self.stacked_widget.setCurrentWidget(self.start)
        self.status_bar.hide()  # start 에서 상태바 숨기기

    def go_to_join(self):
        self.stacked_widget.setCurrentWidget(self.join)
        self.status_bar.show()  # join로 전환 시 상태바 표시

    def go_to_chep(self):
        self.stacked_widget.setCurrentWidget(self.chep)
        self.status_bar.hide()

    def go_to_play(self):
        self.stacked_widget.setCurrentWidget(self.play)
        self.status_bar.show()  # Play 페이지로 전환 시 상태바 표시

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 스타일 파일 로드
    try:
        with open("styles.qss", "r") as f:
            style = f.read()
            app.setStyleSheet(style)  # QSS 파일을 애플리케이션에 적용
    except FileNotFoundError:
        print("styles.qss 파일을 찾을 수 없습니다. 기본 스타일로 실행합니다.")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
