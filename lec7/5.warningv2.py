import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit,
                             QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.users = {
            "user1": "1111",
            "user2": "2222",
            "user3": "3333",
        }
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("5. Warning v2")
        self.user_edit = QLineEdit()
        self.user_edit.setPlaceholderText("User (user1, user2, user3)")
        self.pw_edit = QLineEdit()
        self.pw_edit.setPlaceholderText("Password")
        self.pw_edit.setEchoMode(QLineEdit.EchoMode.Password)
        button = QPushButton("Login")
        button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.user_edit)
        layout.addWidget(self.pw_edit)
        layout.addWidget(button)
        self.setLayout(layout)
        self.show()

    def login(self):
        # 추가: 상황에 맞는 메시지 창 고르기
        user = self.user_edit.text()
        password = self.pw_edit.text()
        if user == "" or password == "":
            QMessageBox.warning(self, "Warning", "Please fill in both fields.")
        elif self.users.get(user) != password:
            QMessageBox.critical(self, "Error", "Wrong user or password.")
        else:
            QMessageBox.information(self, "Welcome", f"Welcome, {user}!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
