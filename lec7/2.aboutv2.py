import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("2. About v2")
        about_button = QPushButton("About")
        about_button.clicked.connect(self.show_about)
        qt_button = QPushButton("About Qt")
        qt_button.clicked.connect(self.show_about_qt)

        layout = QVBoxLayout()
        layout.addWidget(about_button)
        layout.addWidget(qt_button)
        self.setLayout(layout)
        self.show()

    def show_about(self):
        # 추가: HTML 로 꾸미기 (QLabel 처럼 <b>, <br>, <ul> 사용 가능)
        QMessageBox.about(self, "About",
            "<h3>My First App</h3>"
            "<p>Version <b>1.0</b></p>"
            "<ul><li>Signals & Slots</li><li>QMessageBox</li></ul>"
            "<p>Made in GUI Programming class</p>")

    def show_about_qt(self):
        # 추가: Qt 버전 정보를 보여주는 내장 창
        QMessageBox.aboutQt(self, "About Qt")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
