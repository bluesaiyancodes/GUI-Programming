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
        self.setWindowTitle("3. valueChanged")
        # 생성자: 가로 슬라이더
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)                       # 최소값
        self.slider.setMaximum(100)                     # 최대값
        self.slider.setTickInterval(1)                 # tick 간격
        self.slider.setTickPosition(QSlider.TicksBelow) # tick 위치: 아래쪽
        self.slider.setSingleStep(10)                    # 방향키 한 번 = 1
        self.slider.setPageStep(10)                     # PageUp/Down, 빈 곳 클릭 = 10

        # valueChanged: 값이 바뀌면 "어떤 방법이든" 발생
        # (드래그, 방향키, 빈 곳 클릭, 코드의 setValue 모두)
        self.slider.valueChanged.connect(self.on_value_changed)

        button = QPushButton("setValue(50) by code")
        button.clicked.connect(self.change_by_code)

        self.label = QLabel("Signal count: 0\nvalue=0")

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def on_value_changed(self, value):
        snapped = round (value/10)*10
        if snapped != value:
            self.slider.setValue(snapped)
            return
        self.count += 1
        self.label.setText(f"signal count: {self.count}\nvalue={value}")

    def change_by_code(self):
        # 코드로 바꿔도 발생함 -> count 증가 (이미 50이면 변화 없음)
        
        self.slider.setValue(50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

    
