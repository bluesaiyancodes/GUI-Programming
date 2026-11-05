import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QPushButton,
                             QLabel, QVBoxLayout)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("5. sliderPressed")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickInterval(20)
        self.slider.setTickPosition(QSlider.TicksAbove) # tick 위치: 위쪽
        self.slider.setSingleStep(5)
        self.slider.setPageStep(20)

        # sliderPressed: 손잡이(handle)를 "누르는 순간" 한 번만 발생
        # 드래그 중에는 다시 발생하지 않음 / 빈 곳 클릭, 방향키, 코드로는 발생 안 함
        self.slider.sliderPressed.connect(self.on_pressed)
        # 짝꿍: 손잡이를 놓는 순간 발생
        self.slider.sliderReleased.connect(self.on_released)

        button = QPushButton("setValue(50) by code")
        button.clicked.connect(self.change_by_code)

        self.label = QLabel("Press count: 0")
        self.status = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(button)
        layout.addWidget(self.label)
        layout.addWidget(self.status)
        self.setLayout(layout)
        self.show()

    def on_pressed(self):
        # sliderPressed는 값을 넘겨주지 않음 -> value() getter로 가져옴
        self.count += 1
        self.label.setText(f"Press count: {self.count}")
        self.status.setText(f"Pressed at value={self.slider.value()}")

    def on_released(self):
        self.status.setText(self.status.text() +
                            f"\nReleased at value={self.slider.value()}")

    def change_by_code(self):
        # 코드로 바꾸면 sliderPressed는 발생하지 않음 -> count 그대로
        self.slider.setValue(50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
