from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtCore import Qt

class Page1(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # 폰트 로드
        font_id1 = QFontDatabase.addApplicationFont("fonts/전남교육유나체.ttf")
        font_family1 = QFontDatabase.applicationFontFamilies(font_id1)[0]
        font_id2 = QFontDatabase.addApplicationFont("fonts/전남교육또박체.ttf")
        font_family2 = QFontDatabase.applicationFontFamilies(font_id2)[0]

        self.label = QLabel()
        self.button_to_page2 = QPushButton("Go to Page 2")
        self.button_to_page3 = QPushButton("Go to Page 3")

        # text1에 HTML로 글자 간격 조정
        self.label.setText(
            f'''
            <style>
                .div1 {{
                    text-align: center;
                    margin: 0;  
                    padding: 0;  
                }}
                .text1 {{
                    font-family: '{font_family1}';
                    font-size: 80px;
                    margin: 0;  
                    padding: 0;  
                }}
                .text2 {{
                    font-family: '{font_family2}';
                    font-size: 85px;
                    margin: 0;  
                    padding: 0;  
                }}
            </style>
            <div class="div1">
                <p class="text1">꼬리에 꼬리를 무는</p>
                <p class="text2">그 날 이야기</p>
            </div>
            '''
        )

        # 버튼 스타일 설정
        self.button_to_page2.setStyleSheet(""" 
            QPushButton {
                background-color: #3498db;  
                color: white;              
                border-radius: 10px;       
                padding: 10px;             
                font-size: 16px;           
            }
            QPushButton:hover {
                background-color: #2980b9;  
            }
            QPushButton:pressed {
                background-color: #1c598a;  
            }
        """)

        self.button_to_page3.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;  
                color: white;              
                border-radius: 10px;       
                padding: 10px;             
                font-size: 16px;           
            }
            QPushButton:hover {
                background-color: #27ae60;  
            }
            QPushButton:pressed {
                background-color: #1e8449;  
            }
        """)

        self.button_to_page2.setFixedSize(200, 88)
        self.button_to_page3.setFixedSize(200, 88)

        # 버튼 클릭 시 MainWindow의 메서드 호출
        self.button_to_page2.clicked.connect(self.main_window.go_to_page2)
        self.button_to_page3.clicked.connect(self.main_window.go_to_page3)

        # 세로 레이아웃 설정
        layout = QVBoxLayout()
        layout.addSpacing(250)  # label 위에 여백 추가
        layout.addWidget(self.label)
        layout.addSpacing(50)  # label 아래 간격 추가

        # 버튼을 가로로 정렬하기 위한 HBoxLayout
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)  # 버튼 사이의 간격 설정
        button_layout.addWidget(self.button_to_page2)
        button_layout.addWidget(self.button_to_page3)
        button_layout.setAlignment(Qt.AlignCenter)  # 버튼들을 가로 중앙에 정렬

        layout.addLayout(button_layout)  # 버튼 레이아웃을 세로 레이아웃에 추가
        layout.addStretch()  # 아래쪽에 여백 추가

        self.setLayout(layout)
