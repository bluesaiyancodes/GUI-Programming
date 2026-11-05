import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QPushButton,
                             QLabel, QVBoxLayout)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("1. activated")
        self.combo = QComboBox()
        self.combo.addItems(["Apple", "Banana", "Cherry"])
        # activated: 사용자가 마우스/키보드로 직접 고를 때만 발생
        self.combo.activated.connect(self.on_activated)

        button = QPushButton("Change by code (Cherry)")
        button.clicked.connect(self.change_by_code)

        self.label = QLabel("Signal count: 0")

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def on_activated(self, index):
        # 같은 항목을 다시 골라도 발생함
        self.count += 1
        self.label.setText(f"Signal count: {self.count}\n"
                           f"index={index}, text={self.combo.currentText()}")

    def change_by_code(self):
        # 코드로 바꾸면 activated는 발생하지 않음 -> count 그대로
        self.combo.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

