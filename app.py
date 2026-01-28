from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QFormLayout, QHBoxLayout, QMessageBox, QApplication
)
from PyQt6.QtCore import Qt
import sys

from models import create_user


class CreateUserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HISTOSONICS")
        self.setMinimumWidth(350)

        # widgets
        self.username_input = QLineEdit()

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.confirm_input = QLineEdit()
        self.confirm_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.secret_question_input = QLineEdit()
        self.secret_answer_input = QLineEdit()

        # eye buttons
        self.password_eye = QPushButton("👁")
        self.password_eye.setFixedWidth(30)
        self.password_eye.setCheckable(True)
        self.password_eye.clicked.connect(self.toggle_password)

        self.confirm_eye = QPushButton("👁")
        self.confirm_eye.setFixedWidth(30)
        self.confirm_eye.setCheckable(True)
        self.confirm_eye.clicked.connect(self.toggle_confirm)

        # buttons
        self.create_btn = QPushButton("Create User")
        self.cancel_btn = QPushButton("Cancel")

        # style
        button_style = """
            QPushButton {
                background-color: #007BFF;
                color: white;
                padding: 6px 12px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #0069d9;
            }
            QPushButton:pressed {
                background-color: #005cbf;
            }
        """

        self.create_btn.setStyleSheet(button_style)
        self.cancel_btn.setStyleSheet(button_style)

        # layout
        form = QFormLayout()

        form.addRow("Username:", self.username_input)

        pw_layout = QHBoxLayout()
        pw_layout.addWidget(self.password_input)
        pw_layout.addWidget(self.password_eye)
        form.addRow("Password:", pw_layout)

        confirm_layout = QHBoxLayout()
        confirm_layout.addWidget(self.confirm_input)
        confirm_layout.addWidget(self.confirm_eye)
        form.addRow("Confirm Password:", confirm_layout)

        form.addRow("Secret Question:", self.secret_question_input)
        form.addRow("Secret Answer:", self.secret_answer_input)

        btns = QHBoxLayout()
        btns.addWidget(self.cancel_btn)
        btns.addWidget(self.create_btn)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(btns)
        self.setLayout(layout)

        # signals
        self.create_btn.clicked.connect(self.handle_create)
        self.cancel_btn.clicked.connect(self.close)

    def toggle_password(self):
        mode = QLineEdit.EchoMode.Normal if self.password_eye.isChecked() else QLineEdit.EchoMode.Password
        self.password_input.setEchoMode(mode)

    def toggle_confirm(self):
        mode = QLineEdit.EchoMode.Normal if self.confirm_eye.isChecked() else QLineEdit.EchoMode.Password
        self.confirm_input.setEchoMode(mode)

    def handle_create(self):
        username = self.username_input.text().strip()
        password = self.password_input.text()
        confirm = self.confirm_input.text()
        secret_q = self.secret_question_input.text().strip()
        secret_a = self.secret_answer_input.text().strip()

        if not username or not password or not confirm or not secret_q or not secret_a:
            QMessageBox.warning(self, "Missing Fields", "All fields are required.")
            return

        if password != confirm:
            QMessageBox.warning(self, "Password Error", "Passwords do not match.")
            return

        user = create_user(username, password, secret_q, secret_a)

        if user is None:
            QMessageBox.warning(self, "Error", "Username already exists.")
            return

        QMessageBox.information(self, "Success", f"User '{username}' created successfully.")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateUserWindow()
    window.show()
    sys.exit(app.exec())
