import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QSpinBox, QPushButton,
                             QLabel, QVBoxLayout)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("3. textChanged")
        self.spin = QSpinBox()
        self.spin.setRange(0, 100)
        self.spin.setSingleStep(10)
        self.spin.setPrefix("$ ")
        self.spin.setSuffix(" USD")

        # textChanged: 값이 바뀌면 발생 (valueChanged와 같은 시점)
        # 변경된 값을 str로 넘겨줌 -> prefix/suffix도 같이 넘겨짐
        self.spin.textChanged.connect(self.on_text_changed)

        button = QPushButton("setSuffix by code")
        button.clicked.connect(self.change_by_code)

        self.label = QLabel("Signal count: 0\ntext=''")

        layout = QVBoxLayout()
        layout.addWidget(self.spin)
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def on_text_changed(self, text):
        # text는 "$ 50 USD" 같은 str -> 계산에 쓰려면 value() getter 사용
        self.count += 1
        self.label.setText(f"Signal count: {self.count}\n"
                           f"text='{text}' ({type(text).__name__})\n"
                           f"value()={self.spin.value()}")

    def change_by_code(self):
        # 코드로 바꿔도 발생함 -> count 증가 (이미 50이면 변화 없음)
        self.count += 1
        if self.count % 2:
            self.spin.setSuffix(" Won")  # 접미사 바꾸기 (값은 그대로)
        else:
            self.spin.setSuffix(" USD")  # 접미사 바꾸기 (값은 그대로)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
