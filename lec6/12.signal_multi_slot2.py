import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QGridLayout)
from PyQt5.QtCore import Qt, pyqtSignal

class startWindow(QMainWindow):
    # signal 하나: 새 창 크기(width, height)를 함께 보냄
    window_resized = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()

        # 하나의 signal 에 slot 2개 연결
        # init_ui() 의 show() 에서 첫 resizeEvent 가 발생하므로 그 전에 연결해야 함
        self.window_resized.connect(self.update_label)   # slot 1
        self.window_resized.connect(self.resize_box)     # slot 2

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("One Signal, Two Slots")
        layout = QGridLayout()

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label, 0, 0)

        self.label2 = QLabel("", self)
        self.label2.setAl
        self.label2.setStyleSheet("background-color: green; color: white")
        layout.addWidget(self.label2, 1, 0)

        # QMainWindow 에 layout 을 쓰려면 QWidget 을 하나 만들어 central widget 으로
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.show()

    def resizeEvent(self, event):
        # 창 크기가 바뀔 때마다 호출 -> emit 한 번 -> slot 2개 실행
        size = event.size()
        print(f"Resized: {size.width()} x {size.height()} -> emit window_resized")
        self.window_resized.emit(size.width(), size.height())

    def moveEvent(self, event):
        # 창 위치가 바뀔 때마다 호출 (크기는 그대로이므로 slot 1 만 직접 호출)
        pos = event.pos()
        print(f"Moved to: ({pos.x()}, {pos.y()})")
        self.update_label(self.width(), self.height())

    # slot 1: 크기와 위치를 label 에 표시
    def update_label(self, width, height):
        print("slot 1: update_label")
        self.label.setText(
            f"<p>Size: <b>{width} x {height}</b></p>"
            f"<p>Position: <b>({self.x()}, {self.y()})</b></p>")

    # slot 2: 창 크기에 맞춰 아래 상자 크기 변경 (창의 1/2 x 1/3)
    def resize_box(self, width, height):
        print("slot 2: resize_box")
        box_w, box_h = width // 2, height // 3
        # setFixedSize 를 쓰면 창을 줄일 때 상자가 막아서 잘 안 줄어듦 -> 최대 크기만 지정
        self.label2.setMaximumSize(box_w, box_h)
        self.label2.setText(f"Box: {box_w} x {box_h}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
