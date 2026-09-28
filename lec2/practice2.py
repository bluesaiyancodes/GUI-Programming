import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("실습 2 - 사용자 정보 입력")
window.setFixedSize(450, 350)

lbl = QLabel("환영합니다!", window)
lbl.setAlignment(Qt.AlignCenter)
lbl.resize(250, 30)
lbl.move(100, 70)

le = QLineEdit(window)
le.setPlaceholderText("이름을 입력하세요")
le.resize(250, 30)
le.move(100, 130)

def on_click_confirm():
    name = le.text()
    if name:
        #lbl.setText(f"{name}님 환영합니다!")
        label2.setText(f"{name}님 환영합니다!")
        image_label.show()
        window2.show()

    else:
        lbl.setText("이름을 입력해주세요!")

def on_click_clear():
    le.clear()
    lbl.setText("환영합니다!")
    window2.hide()

btn_ok = QPushButton("확인", window)
btn_ok.resize(120, 35)
btn_ok.move(95, 190)
btn_ok.clicked.connect(on_click_confirm)

btn_clear = QPushButton("지우기", window)
btn_clear.resize(120, 35)
btn_clear.move(235, 190)
btn_clear.clicked.connect(on_click_clear)



window2 = QWidget()
window2.setWindowTitle("Window 2")
window2.setStyleSheet("background-color: lightyellow;")
window2.setFixedSize(450, 350)

label2 = QLabel("Window 2", window2)
label2.setStyleSheet("font-size: 18px; font-weight: bold; color: darkorange;")
label2.resize(350, 100)
label2.setAlignment(Qt.AlignCenter)
"\\" 

pixmap = QPixmap("/Users/blue/Library/CloudStorage/GoogleDrive-bishalrswain@gmail.com/My Drive/South Korea/KIT/Lecture/2026-2 GUI_programming/workspace/assets/image.png")  # 이미지 파일 경로를 지정하세요
image_label = QLabel(window2)
image_label.resize(200, 200)
image_label.move(125, 150)
image_label.setPixmap(pixmap)
image_label.setScaledContents(True) 


window.show()
sys.exit(app.exec_())