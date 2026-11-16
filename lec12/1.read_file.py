import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QPlainTextEdit, QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 실행 위치가 달라도 이 .py 파일을 기준으로 경로를 찾음
        self.file_path = Path(__file__).resolve().parent / "samples" / "hello.txt"
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("1. Read a text file")
        self.resize(580, 340)

        button = QPushButton("Read file ('r')")
        button.clicked.connect(self.read_file)

        self.label = QLabel(str(self.file_path))
        self.label.setTextFormat(Qt.PlainText)
        self.label.setWordWrap(True)
        self.preview = QPlainTextEdit()
        self.preview.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.label)
        layout.addWidget(self.preview)
        self.setLayout(layout)
        self.show()

    def read_file(self):
        try:
            # 'r': 읽기 / encoding='utf-8': 한글도 올바르게 읽음
            # with 블록이 끝나면 파일이 자동으로 닫힘
            with open(self.file_path, "r", encoding="utf-8") as file:
                text = file.read()       # 파일 전체 -> str
        except (OSError, UnicodeError) as error:
            QMessageBox.warning(self, "Read error", str(error))
            return

        self.preview.setPlainText(text)
        self.label.setText(f"{self.file_path}\nRead {len(text)} characters.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())

