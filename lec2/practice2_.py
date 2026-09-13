import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("실습 2 - 사용자 정보 입력")
window.setFixedSize(450, 350)

label1 = QLabel("환영합니다!", window)
label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
#label1.resize(250, 30)
#label1.move(100, 70)

line_edit = QLineEdit(window)
line_edit.setPlaceholderText("이름을 입력하세요")
line_edit.resize(250, 30)
line_edit.move(100, 130)







window.show()
sys.exit(app.exec_())