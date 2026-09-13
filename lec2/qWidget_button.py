import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt

def on_click():
    print("버튼이 눌렸습니다")

app = QApplication(sys.argv)
window = QWidget()
window.resize(300,50)

button = QPushButton("확인", window)
button.clicked.connect(on_click)


window.show()
sys.exit(app.exec())