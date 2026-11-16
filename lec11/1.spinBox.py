import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QSpinBox, QPushButton,
                             QLabel, QVBoxLayout)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("1. QSpinBox")
        # QSpinBox: int 값을 직접 입력하거나 증가/감소 버튼으로 조절
        self.spin = QSpinBox()
        self.spin.setMinimum(0)             # 최소값
        self.spin.setMaximum(100)           # 최대값
        # self.spin.setRange(0, 100)        # 위 두 줄을 한 번에 설정
        self.spin.setSingleStep(5)          # 증가/감소 버튼, 방향키 한 번 = 5 (int)
        self.spin.setPrefix("$ ")           # 접두사: 값 앞에 표시 (달러 기호 등)
        self.spin.setSuffix(" USD")         # 접미사: 값 뒤에 표시 (unit 등)
        self.spin.setValue(20)              # setter: 현재 값 설정
        self.count = 0

        set_button = QPushButton("setValue(150) by code")
        set_button.clicked.connect(self.change_by_code)

        get_button = QPushButton("Read value()")
        get_button.clicked.connect(self.read_value)

        self.label = QLabel("Press 'Read value()'")

        layout = QVBoxLayout()
        layout.addWidget(self.spin)
        layout.addWidget(set_button)
        layout.addWidget(get_button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def change_by_code(self):
        # 범위(0~100) 밖의 값을 넣으면 최대값 100으로 맞춰짐
        #self.spin.setValue(150)
        self.count += 1
        if self.count % 2:
            self.spin.setSuffix(" Won")  # 접미사 바꾸기 (값은 그대로)
        else:
            self.spin.setSuffix(" USD")  # 접미사 바꾸기 (값은 그대로)

    def read_value(self):
        # getter: value()는 prefix/suffix 없이 숫자(int)만 돌려줌
        value = self.spin.value()
        self.label.setText(f"value() = {value} ({type(value).__name__})\n"
                           f"text() = '{self.spin.text()}'")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

    
