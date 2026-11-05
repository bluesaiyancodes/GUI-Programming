import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QPushButton,
                             QLabel, QVBoxLayout)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("2. currentIndexChanged")
        self.combo = QComboBox()
        self.combo.addItems(["Apple", "Banana", "Cherry"])
        # currentIndexChanged: 인덱스가 "바뀔 때마다" 발생 (사용자 + 코드 모두)
        self.combo.currentIndexChanged.connect(self.on_index_changed)

        button = QPushButton("Change by code (Cherry)")
        button.clicked.connect(self.change_by_code)

        self.label = QLabel("Signal count: 0")

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def on_index_changed(self, index):
        # 같은 항목을 다시 고르면 인덱스가 안 바뀌므로 발생하지 않음
        self.count += 1
        self.label.setText(f"Signal count: {self.count}\n"
                           f"index={index}, text={self.combo.currentText()}")

    def change_by_code(self):
        # 코드로 바꿔도 발생함 -> count 증가 (이미 Cherry면 변화 없음)
        self.combo.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

