import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QGridLayout,
)
from PyQt5.QtCore import Qt


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QGridLayout")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #f0f0f0;")

        # Create grid layout
        layout = QGridLayout()

        # addWidget(widget, row, column)
        label = QLabel("그리드 (0, 0)", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color: red; color: black; font-size: 24px;"
        )
        layout.addWidget(label, 0, 0)

        label = QLabel("그리드 (0, 1)", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color: blue; color: black; font-size: 24px;"
        )
        layout.addWidget(label, 0, 1)

        label = QLabel("그리드 (1, 0)", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color: green; color: black; font-size: 24px;"
        )
        layout.addWidget(label, 1, 0)

        label = QLabel("그리드 (1, 1)", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color: yellow; color: black; font-size: 24px;"
        )
        layout.addWidget(label, 1, 1)

        # addWidget(widget, row, column, rowSpan, columnSpan)
        label = QLabel("그리드 (2, 0) - 2칸 병합", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color: orange; color: black; font-size: 24px;"
        )
        layout.addWidget(label, 2, 0, 1, 2)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())
