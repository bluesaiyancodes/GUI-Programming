import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap

from pathlib import Path
img_path = Path(__file__).parent.parent / "assets" / "image.png"


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("실습 2 - 사용자 정보 입력")
window.setFixedSize(450, 350)


image_label = QLabel(window)
image_label.setGeometry(100, 100, 250, 200) # 위치 (100, 100), 크기 250x200
pixmap = QPixmap(str(img_path))
image_label.setPixmap(pixmap)
image_label.setScaledContents(True)



window.show()
sys.exit(app.exec_())