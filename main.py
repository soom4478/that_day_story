import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from page1 import Page1
from page2 import Page2
from page3 import Page3
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
        self.page1 = Page1(self)
        self.page2 = Page2(self)
        self.page3 = Page3(self)
        self.play = Play(self)  # Play 인스턴스 생성
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        self.stacked_widget.addWidget(self.play)

        # 커스텀 상태바 설정
        self.status_bar = CustomStatusBar(self)
        self.setStatusBar(self.status_bar)
        self.status_bar.hide()  # 기본적으로 상태바 숨기기

        # 초기 화면을 Play으로 설정
        self.stacked_widget.setCurrentWidget(self.play)

    # 페이지 전환 메서드들 정의
    def go_to_page2(self):
        self.stacked_widget.setCurrentWidget(self.page2)
        self.status_bar.hide()  # Page2에서는 상태바 숨기기

    def go_to_page1(self):
        self.stacked_widget.setCurrentWidget(self.page1)
        self.status_bar.hide()  # Page1에서는 상태바 숨기기

    def go_to_page3(self):
        self.stacked_widget.setCurrentWidget(self.page3)
        self.status_bar.show()  # Page3로 전환 시 상태바 표시

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
