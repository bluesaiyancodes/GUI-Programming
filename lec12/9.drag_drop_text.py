import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QFrame, QVBoxLayout)


class DropLabel(QLabel):
    def __init__(self):
        super().__init__("Drop selected text here.")
        self.setAcceptDrops(True)
        self.setTextFormat(Qt.PlainText)  # <b> 같은 문자열도 그대로 표시
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignCenter)
        self.setFrameShape(QFrame.StyledPanel)
        self.setMinimumHeight(180)

    def dragEnterEvent(self, event):
        # 파일 URL도 hasText()가 True일 수 있으므로 URL은 제외
        data = event.mimeData()
        if data.hasText() and not data.hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        data = event.mimeData()
        if not data.hasText() or data.hasUrls():
            event.ignore()
            return

        self.setText(data.text())       # MIME 데이터에서 str 읽기
        event.setDropAction(Qt.CopyAction)  # 원본 텍스트를 유지
        event.accept()


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("9. Drag and drop text")
        self.resize(560, 300)
        self.source = QLineEdit("Select these words, then drag them down.")
        self.source.setDragEnabled(True)   # 선택한 글자를 drag할 수 있게 함
        self.target = DropLabel()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Select text; press and hold on the selection to drag."))
        layout.addWidget(self.source)
        layout.addWidget(self.target)
        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
