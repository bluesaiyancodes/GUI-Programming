import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("실습 1") 
window.resize(500, 400) 
window.setStyleSheet("background-color: lightgreen") 

lbl = QLabel("안녕하세요, PyQt5!", window) 
lbl.move(180, 150) 

btn = QPushButton("클릭", window) 
btn.resize(120, 40) 
btn.move(190, 200) 

window.show() 
sys.exit(app.exec_()) 