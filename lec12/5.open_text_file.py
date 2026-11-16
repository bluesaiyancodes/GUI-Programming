import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QPlainTextEdit, QVBoxLayout, QFileDialog, QMessageBox)


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("5. Open and read a text file")
        self.resize(640, 400)
        button = QPushButton("Open text file")
        button.clicked.connect(self.open_file)
        self.label = QLabel("Choose a UTF-8 text file (up to 1 MB).")
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

    def open_file(self):
        file_name, selected_filter = QFileDialog.getOpenFileName(
            self, "Open text file", str(Path(__file__).resolve().parent / "samples"),
            "Text files (*.txt *.md *.py);;All files (*)")
        if not file_name:
            return

        try:
            # 큰 파일로 GUI가 멈추지 않도록 읽는 양을 제한
            with open(file_name, "rb") as file:
                data = file.read(1_000_001) # 1_000_001은 1 MB + 1 byte
            if len(data) > 1_000_000:
                QMessageBox.warning(self, "File too large", "Choose a file up to 1 MB.")
                return
            # utf-8-sig는 일반 UTF-8과 Windows의 UTF-8 BOM을 모두 처리
            text = data.decode("utf-8-sig")
        except (OSError, UnicodeError) as error:
            QMessageBox.warning(self, "Open error", f"Choose a UTF-8 text file.\n{error}")
            return

        # 실패하거나 취소하면 이전 미리보기를 유지
        self.preview.setPlainText(text)
        self.label.setText(f"{file_name}\n{len(text)} characters")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
