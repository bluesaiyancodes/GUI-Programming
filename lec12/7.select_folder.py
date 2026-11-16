import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QListWidget, QVBoxLayout, QFileDialog, QMessageBox)


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("7. Select a folder")
        self.resize(600, 360)
        button = QPushButton("Select folder")
        button.clicked.connect(self.select_folder)
        self.label = QLabel("No folder selected.")
        self.label.setTextFormat(Qt.PlainText)
        self.label.setWordWrap(True)
        self.file_list = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.label)
        layout.addWidget(self.file_list)
        self.setLayout(layout)
        self.show()

    def select_folder(self):
        # getExistingDirectory는 튜플이 아닌 폴더 경로 str 하나를 반환
        folder = QFileDialog.getExistingDirectory(
            self, "Select folder", str(Path(__file__).resolve().parent))
        if not folder:
            return

        try:
            # iterdir(): 바로 아래 항목만 나열 (하위 폴더 안은 탐색하지 않음)
            paths = sorted(Path(folder).iterdir(), key=lambda path: path.name.lower())
            items = []
            for path in paths:
                kind = "Folder" if path.is_dir() else "File"
                items.append(f"[{kind}] {path.name}")
        except OSError as error:
            QMessageBox.warning(self, "Folder error", str(error))
            return

        self.file_list.clear()
        self.file_list.addItems(items)
        self.label.setText(f"{folder}\n{len(items)} items")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
