import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit,
                             QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("1. Information v2")
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Name")
        self.age_edit = QLineEdit()
        self.age_edit.setPlaceholderText("Age")
        button = QPushButton("Submit")
        button.clicked.connect(self.show_info)

        layout = QVBoxLayout()
        layout.addWidget(self.name_edit)
        layout.addWidget(self.age_edit)
        layout.addWidget(button)
        self.setLayout(layout)
        self.show()

    def show_info(self):
        # 추가: 입력한 내용으로 메시지를 만듦
        name = self.name_edit.text()
        age = self.age_edit.text()
        QMessageBox.information(self, "Submitted",
                                f"Name: {name}\nAge: {age}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
