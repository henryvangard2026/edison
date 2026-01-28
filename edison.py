from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QFormLayout, QHBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt


class CreateUserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HISTOSONICS")
        self.setMinimumWidth(350)

        # the widgets 
        self.username_input = QLineEdit()

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.confirm_input = QLineEdit()
        self.confirm_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.secret_question_input = QLineEdit()
        self.secret_answer_input = QLineEdit()

        # widgets for the eye icon next to the password fields
        self.password_eye = QPushButton("👁")
        self.password_eye.setFixedWidth(30)
        self.password_eye.setCheckable(True)
        self.password_eye.clicked.connect(self.toggle_password)

        self.confirm_eye = QPushButton("👁")
        self.confirm_eye.setFixedWidth(30)
        self.confirm_eye.setCheckable(True)
        self.confirm_eye.clicked.connect(self.toggle_confirm)

        # the buttons
        self.create_btn = QPushButton("Create User")
        self.cancel_btn = QPushButton("Cancel")
        
        # make both buttons blue
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
        
        # layouts for the eye icons
        form_layout = QFormLayout()

        form_layout.addRow("Username:", self.username_input)

        # password row
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_input)
        password_layout.addWidget(self.password_eye)
        form_layout.addRow("Password:", password_layout)

        # confirm password row
        confirm_layout = QHBoxLayout()
        confirm_layout.addWidget(self.confirm_input)
        confirm_layout.addWidget(self.confirm_eye)
        form_layout.addRow("Confirm Password:", confirm_layout)

        form_layout.addRow("Secret Question:", self.secret_question_input)
        form_layout.addRow("Secret Answer:", self.secret_answer_input)

        # buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.cancel_btn)
        button_layout.addWidget(self.create_btn)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    # toggle password visibility
    def toggle_password(self):
        if self.password_eye.isChecked():
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    # toggle confirm visibility
    def toggle_confirm(self):
        if self.confirm_eye.isChecked():
            self.confirm_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.confirm_input.setEchoMode(QLineEdit.EchoMode.Password)

    # event handlers (logic)
    def handle_create(self):
        username = self.username_input.text().strip()
        password = self.password_input.text()
        confirm = self.confirm_input.text()
        secret_q = self.secret_question_input.text().strip()
        secret_a = self.secret_answer_input.text().strip()

        # Basic validation
        if not username or not password or not confirm or not secret_q or not secret_a:
            QMessageBox.warning(self, "Missing Fields", "All fields are required.")
            return

        if password != confirm:
            QMessageBox.warning(self, "Password Error", "Passwords do not match.")
            return

        QMessageBox.information(self, "Success", f"User '{username}' created successfully.")
        self.close()


# main
if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = CreateUserWindow()
    window.show()
    sys.exit(app.exec())
