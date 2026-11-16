import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QListWidget,
                             QVBoxLayout)


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("8. Drag and drop files")
        self.resize(640, 340)
        self.setAcceptDrops(True)       # 이 창에서 drop 이벤트 받기
        self.label = QLabel("Drop files from File Explorer / Finder here.")
        self.label.setWordWrap(True)
        self.file_list = QListWidget()
        # 자식 위젯이 drop을 가로채지 않도록 부모 창에서 처리
        self.file_list.setAcceptDrops(False)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.file_list)
        self.setLayout(layout)
        self.show()

    def local_files(self, mime_data):
        # 파일은 문자열이 아닌 URL 목록(text/uri-list)으로 전달됨
        paths = []
        if mime_data.hasUrls():
            for url in mime_data.urls():
                if url.isLocalFile():    # 웹 주소 제외
                    path = Path(url.toLocalFile())  # 공백/한글 경로도 처리
                    if path.is_file():  # 폴더 제외
                        paths.append(str(path))
        return paths

    def dragEnterEvent(self, event):
        # 수락해야 이후 dropEvent를 받을 수 있음
        if self.local_files(event.mimeData()):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        paths = self.local_files(event.mimeData())
        if not paths:
            event.ignore()
            return

        self.file_list.clear()
        self.file_list.addItems(paths)
        self.label.setText(f"Dropped: {len(paths)} files (paths only)")
        # 경로만 표시함. 실제 파일은 복사하거나 이동하지 않음
        # CopyAction으로 응답하여 원본 삭제/이동을 요청하지 않음
        event.setDropAction(Qt.CopyAction)
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
