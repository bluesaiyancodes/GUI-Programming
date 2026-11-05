import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QPushButton,
                             QLabel, QHBoxLayout, QVBoxLayout)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("4. sliderMoved")
        # 생성자: 세로 슬라이더
        self.slider = QSlider(Qt.Vertical)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksBothSides) # tick 위치: 양쪽
        self.slider.setSingleStep(1)
        self.slider.setPageStep(10)

        # sliderMoved: 사용자가 손잡이(handle)를 "드래그하는 동안"만 발생
        # 방향키, 빈 곳 클릭, 코드의 setValue로는 발생하지 않음
        self.slider.sliderMoved.connect(self.on_slider_moved)

        button = QPushButton("setValue(50) by code")
        button.clicked.connect(self.change_by_code)

        self.label = QLabel("Signal count: 0\nvalue=0")

        right = QVBoxLayout()
        right.addWidget(button)
        right.addWidget(self.label)

        layout = QHBoxLayout()
        layout.addWidget(self.slider)
        layout.addLayout(right)
        self.setLayout(layout)
        self.show()

    def on_slider_moved(self, value):
        self.count += 1
        self.label.setText(f"Signal count: {self.count}\nvalue={value}")

    def change_by_code(self):
        # 코드로 바꾸면 sliderMoved는 발생하지 않음 -> count 그대로
        self.slider.setValue(50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
