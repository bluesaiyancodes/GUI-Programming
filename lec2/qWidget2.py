import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt5 GUI")
window.resize(400, 320)
window.setStyleSheet("background-color: lightblue")

lbl = QLabel("안녕하세요", window)
lbl.move(160, 90)

lbl.setText("hello")

name_lbl = QLabel("이름을 입력해주세요:", window)
name_lbl.move(120, 120)
edit = QLineEdit(window)
edit.move(120, 150)




btn = QPushButton("확인", window)
btn.resize(100, 40)
btn.move(130, 190)

window.show()
sys.exit(app.exec_())
