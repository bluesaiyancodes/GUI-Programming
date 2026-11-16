import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QPlainTextEdit, QHBoxLayout, QVBoxLayout, QMessageBox)


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.file_path = Path(__file__).resolve().parent / "output" / "notes.txt"
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("2. Write vs append")
        self.resize(580, 450)

        self.editor = QPlainTextEdit()
        self.editor.setPlainText("Hello, file!\n안녕하세요!")
        write_button = QPushButton("Write ('w')")
        write_button.clicked.connect(lambda: self.write_file("w"))
        append_button = QPushButton("Append ('a')")
        append_button.clicked.connect(lambda: self.write_file("a"))
        read_button = QPushButton("Read saved file")
        read_button.clicked.connect(self.read_file)

        buttons = QHBoxLayout()
        buttons.addWidget(write_button)
        buttons.addWidget(append_button)
        buttons.addWidget(read_button)

        self.label = QLabel(f"Output: {self.file_path}")
        self.label.setTextFormat(Qt.PlainText)
        self.label.setWordWrap(True)
        self.preview = QPlainTextEdit()
        self.preview.setReadOnly(True)
        self.preview.setPlaceholderText("Saved contents appear here.")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Text to write (a newline is added at the end):"))
        layout.addWidget(self.editor)
        layout.addLayout(buttons)
        layout.addWidget(self.label)
        layout.addWidget(self.preview)
        self.setLayout(layout)
        self.show()

    def write_file(self, mode):
        # 'w': 기존 내용을 지우고 쓰기 / 'a': 기존 내용 뒤에 추가
        if mode == "w" and self.file_path.exists():
            answer = QMessageBox.question(
                self, "Overwrite?", "Replace the contents of notes.txt?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if answer != QMessageBox.Yes:
                return

        text = self.editor.toPlainText()
        if not text.endswith("\n"):
            text += "\n"
        try:
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.file_path, mode, encoding="utf-8") as file:
                file.write(text)
        except (OSError, UnicodeError) as error:
            QMessageBox.warning(self, "Write error", str(error))
            return

        self.read_file()

    def read_file(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                text = file.read()
        except (OSError, UnicodeError) as error:
            QMessageBox.warning(self, "Read error", str(error))
            return
        self.preview.setPlainText(text)
        self.label.setText(f"Saved file: {self.file_path}\n{len(text)} characters")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
