import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt


def on_click():
    user_message = line_edit1.text()
    #label1.setText(user_message)
    if user_message:
        label2.setText(user_message)
        window2.show()

app = QApplication(sys.argv)


window1 = QWidget()
window1.setWindowTitle("Window 1")
window1.setStyleSheet("background-color: lightblue;")
window1.setFixedSize(450, 350)


label1 = QLabel("9월 14일 월요일입니다", window1)
label1.setStyleSheet("font-size: 18px; font-weight: bold; color: darkblue;")
label1.resize(350, 100)
label1.setAlignment(Qt.AlignCenter)

line_edit1 = QLineEdit(window1)
line_edit1.resize(250, 30)
line_edit1.move(100, 150)
line_edit1.setStyleSheet("font-size: 14px; padding: 5px; border: 2px solid darkblue; border-radius: 10px; font-weight: bold; color: darkblue;")

#line_edit1.setText("이름을 적어주세용")
line_edit1.setPlaceholderText("이름을 적어주세용")

window2 = QWidget()
window2.setWindowTitle("Window 2")
window2.setStyleSheet("background-color: lightyellow;")
window2.setFixedSize(450, 350)

label2 = QLabel("Window 2", window2)
label2.setStyleSheet("font-size: 18px; font-weight: bold; color: darkorange;")
label2.resize(350, 100)
label2.setAlignment(Qt.AlignCenter)



button1 = QPushButton("change", window1)
button1.setStyleSheet("background-color: lightgreen; font-size: 16px; font-weight: bold; color: darkgreen;")
button1.resize(100, 50)
button1.move(175, 200)
button1.clicked.connect(on_click)


window1.show()
sys.exit(app.exec_())



