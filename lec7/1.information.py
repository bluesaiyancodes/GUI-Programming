import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("1. Information")
        button = QPushButton("Show Info")
        button.clicked.connect(self.show_info)
        self.label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def show_info(self):
        # QMessageBox.information(부모, 제목, 내용)
        QMessageBox.information(self, "Info", "[File] saved successfully.")
        # 메시지 창을 닫아야 다음 줄이 실행됨
        self.label.setText("Info box closed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

