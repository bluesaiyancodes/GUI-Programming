import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDoubleSpinBox, QPushButton,
                             QLabel, QVBoxLayout)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("4. QDoubleSpinBox")
        # QDoubleSpinBox: QSpinBox와 같지만 float 값을 다룸
        self.spin = QDoubleSpinBox()
        self.spin.setRange(0.0, 10.0)       # 범위도 float로 설정
        self.spin.setDecimals(1)            # 소수점 자리수 (기본값 2)
        self.spin.setSingleStep(0.5)        # 증가/감소 버튼 한 번 = 0.5 (float)
        self.spin.setSuffix(" kg")

        # valueChanged: QSpinBox와 같은 signal이지만 float를 넘겨줌
        self.spin.valueChanged.connect(self.on_value_changed)

        button = QPushButton("setValue(3.14) by code")
        button.clicked.connect(self.change_by_code)

        self.label = QLabel("Signal count: 0\nvalue=0.0")

        layout = QVBoxLayout()
        layout.addWidget(self.spin)
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def on_value_changed(self, value):
        self.count += 1
        self.label.setText(f"Signal count: {self.count}\n"
                           f"value={value} ({type(value).__name__})")

    def change_by_code(self):
        # decimals=1 이므로 3.14 -> 3.1로 반올림되어 저장됨
        # 두 번째 클릭부터는 이미 3.1이라 변화 없음 -> count 그대로
        self.spin.setValue(3.14)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
