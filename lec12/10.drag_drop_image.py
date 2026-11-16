import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                             QSizePolicy)


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.pixmap = QPixmap()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("10. Drop an image file")
        self.resize(600, 420)
        self.setAcceptDrops(True)
        self.label = QLabel("Drop ONE image file: PNG, JPG, JPEG, BMP, or GIF.")
        self.label.setTextFormat(Qt.PlainText)
        self.label.setWordWrap(True)
        self.image = QLabel("Image preview")
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setMinimumSize(360, 240)
        # 원본 이미지 크기 때문에 창이 커지는 것을 방지
        self.image.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.image, 1)
        self.setLayout(layout)
        self.show()

    def image_path(self, mime_data):
        urls = mime_data.urls()
        if len(urls) != 1 or not urls[0].isLocalFile():
            return None
        path = Path(urls[0].toLocalFile())
        if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".bmp", ".gif"}:
            return path
        return None

    def dragEnterEvent(self, event):
        if self.image_path(event.mimeData()) is not None:
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        path = self.image_path(event.mimeData())
        if path is None:
            event.ignore()
            return

        pixmap = QPixmap(str(path))
        # 확장자가 이미지여도 실제 내용이 손상되었으면 읽을 수 없음
        if pixmap.isNull():
            self.label.setText("Cannot read this image. Previous preview kept.")
            event.ignore()
            return

        self.pixmap = pixmap
        self.show_image()
        self.label.setText(f"{path.name}\n{pixmap.width()} x {pixmap.height()} pixels")
        event.setDropAction(Qt.CopyAction)
        event.accept()

    def show_image(self):
        if not self.pixmap.isNull():
            # 원본은 보관하고, 미리보기만 비율을 유지하며 조절
            self.image.setPixmap(self.pixmap.scaled(
                self.image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.show_image()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
