import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit,
                             QLabel, QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("4. Critical v2")
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Enter a number")
        button = QPushButton("Calculate 100 / number")
        button.clicked.connect(self.divide)
        self.label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def divide(self):
        # 추가: 실제 오류(예외)가 나면 critical 로 알려줌
        try:
            number = float(self.edit.text())
            self.label.setText(f"100 / {number} = {100 / number}")
        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter a number.")
        except ZeroDivisionError:
            QMessageBox.critical(self, "Error", "Cannot divide by zero!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
