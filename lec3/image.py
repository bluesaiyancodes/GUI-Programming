import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap

from pathlib import Path
img_path = Path(__file__).parent.parent / "assets" / "image.png"
print(img_path)

def on_click_change():
    img_path2 = Path(__file__).parent.parent / "assets" / "woni.jpeg"
    pixmap = QPixmap(str(img_path2))
    image_label.setPixmap(pixmap)
    image_label.setScaledContents(True)  # 이미지 크기를 QLabel에 맞게 조정
    

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("실습 2 - 사용자 정보 입력")
window.setFixedSize(450, 350)


image_label = QLabel(window)
image_label.setGeometry(100, 100, 250, 200) # 위치 (100, 100), 크기 250x200
pixmap = QPixmap(str(img_path))
image_label.setPixmap(pixmap)
image_label.setScaledContents(True)

btn_ok = QPushButton("아이유 말고 원이", window)
btn_ok.setGeometry(150, 50, 150, 50)
btn_ok.clicked.connect(on_click_change)



window.show()
sys.exit(app.exec_())