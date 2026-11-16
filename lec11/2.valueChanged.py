import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QSpinBox, QPushButton,
                             QLabel, QVBoxLayout)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("2. valueChanged")
        self.spin = QSpinBox()
        self.spin.setRange(0, 100)          # 최소값, 최대값을 한 번에 설정
        self.spin.setSingleStep(10)         # 증가/감소 버튼, 방향키 한 번 = 10
        self.spin.setPrefix("$ ")
        self.spin.setSuffix(" USD")

        # valueChanged: 값이 바뀌면 "어떤 방법이든" 발생
        # (증가/감소 버튼, 방향키, 직접 입력, 코드의 setValue 모두)
        # 변경된 값을 int로 넘겨줌 -> prefix/suffix는 포함되지 않음
        self.spin.valueChanged.connect(self.on_value_changed)

        button = QPushButton("setValue(50) by code")
        button.clicked.connect(self.change_by_code)

        self.label = QLabel("Signal count: 0\nvalue=0")

        layout = QVBoxLayout()
        layout.addWidget(self.spin)
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def on_value_changed(self, value):
        # 직접 입력할 때는 한 글자 칠 때마다 발생 (예: 45 입력 -> 4, 45 두 번)
        self.count += 1
        self.label.setText(f"Signal count: {self.count}\n"
                           f"value={value} ({type(value).__name__})")

    def change_by_code(self):
        # 코드로 바꿔도 발생함 -> count 증가 (이미 50이면 변화 없음)
        self.spin.setValue(50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
