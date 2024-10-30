from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton

class Page2(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.label = QLabel("This is Page 2")
        self.button_to_page1 = QPushButton("Go to Page 1")
        self.button_to_page3 = QPushButton("Go to Page 3")

        # 버튼 클릭 시 MainWindow의 메서드 호출
        self.button_to_page1.clicked.connect(self.main_window.go_to_page1)
        self.button_to_page3.clicked.connect(self.main_window.go_to_page3)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_to_page1)
        layout.addWidget(self.button_to_page3)
        self.setLayout(layout)
