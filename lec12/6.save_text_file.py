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
        self.setWindowTitle("6. Save text as a file")
        self.resize(640, 400)
        self.editor = QPlainTextEdit()
        self.editor.setPlainText("My first saved text file.\n나의 첫 번째 텍스트 파일!")
        button = QPushButton("Save As...")
        button.clicked.connect(self.save_file)
        self.label = QLabel("Edit the text, then save it before closing.")
        self.label.setTextFormat(Qt.PlainText)
        self.label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def save_file(self):
        # 대화상자는 경로만 반환함 -> 실제 저장은 open()/write()로 수행
        # 기본 설정에서는 기존 파일을 선택하면 덮어쓰기 확인을 표시
        file_name, selected_filter = QFileDialog.getSaveFileName(
            self, "Save text file", str(Path.home() / "note.txt"),
            "Text files (*.txt);;All files (*)")
        if not file_name:
            return

        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(self.editor.toPlainText())
        except (OSError, UnicodeError) as error:
            QMessageBox.warning(self, "Save error", str(error))
            return

        self.label.setText(f"Saved: {file_name}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
