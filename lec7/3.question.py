import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("3. Question")
        button = QPushButton("Ask")
        button.clicked.connect(self.ask)
        self.label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def ask(self):
        # question 은 사용자가 누른 버튼을 돌려줌
        answer = QMessageBox.question(self, "Question", "Do you like Python?")
        if answer == QMessageBox.StandardButton.Yes:
            self.label.setText("You chose Yes 😊")
        else:
            self.label.setText("You chose No 😢")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
