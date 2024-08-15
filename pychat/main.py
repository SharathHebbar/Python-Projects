import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QTextEdit, QLineEdit, QPushButton, QListWidget, QSplitter, QFileDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont

class ChatApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatBot")
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(QIcon("Image.jpg"))

        style = '''
            QMainWindow {
                background-color: #1e1e1e;
                font-family: 'Segoe UI', sans-serif;
            }

            QTextEdit {
                background-color: #2d2d2d;
                color: #dcdcdc;
                border-radius: 8px;
                padding: 12px;
                font-size: 16px;
                border: none;
            }

            QLineEdit {
                background-color: #2d2d2d;
                color: #dcdcdc;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                border: 1px solid #ddd;
            }

            QPushButton {
                background-color: #ffffff;
                color: #000;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                border: 1px solid #ddd;
            }

            QPushButton:hover {
               background-color: #ffffff;
               color: #000;
            }

            QListWidget {
                background-color: #2d2d2d;
                color: #dcdcdc;
                border-radius: 8px;
                padding: 12px;
                font-size: 16px;
                border: none;
            }
        '''
        self.setStyleSheet(style)

        splitter = QSplitter(Qt.Horizontal)
        left_pane = QWidget()
        main_content = QWidget()

        left_layout = QVBoxLayout()
        new_chat_button = QPushButton("+ New Chat")
        new_chat_button.setFont(QFont('Segoe UI', 12))
        new_chat_button.clicked.connect(self.new_chat)
        self.chat_list = QListWidget()

        left_layout.addWidget(new_chat_button)
        left_layout.addWidget(self.chat_list)
        left_pane.setLayout(left_layout)

        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        self.chat_history.setPlaceholderText("Chat history...")

        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Type a message...")

        self.attachment_button = QPushButton("")
        self.attachment_button.setIcon(QIcon(r"assets\upload.png"))
        # self.attachment_button.setIconSize(self.user_input.sizeHint())
        self.attachment_button.clicked.connect(self.attach_file)

        self.send_button = QPushButton("")
        self.send_button.setIcon(QIcon(r"assets\send.png"))
        # self.send_button.setIconSize(self.user_input.sizeHint())

        self.send_button.clicked.connect(self.send_message)

        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()

        input_layout.addWidget(self.user_input)
        input_layout.addWidget(self.attachment_button)
        input_layout.addWidget(self.send_button)

        main_layout.addWidget(self.chat_history)
        main_layout.addLayout(input_layout)
        main_content.setLayout(main_layout)

        splitter.addWidget(left_pane)
        splitter.addWidget(main_content)

        self.setCentralWidget(splitter)

        self.current_chat = []

    def new_chat(self):
        self.current_chat = []
        self.chat_history.clear()
        self.chat_list.addItem("Chat " + str(self.chat_list.count() + 1))

    def send_message(self):
        user_message = self.user_input.text().strip()
        if user_message:
            self.user_input.clear()
            self.chat_history.append("<b>User:</b> " + user_message)
            self.current_chat.append("<b>User:</b> " + user_message)
            self.handle_message(user_message)

    def handle_message(self, message):
        response = self.get_response(message)
        self.chat_history.append("<b>Response:</b> " + response)
        self.current_chat.append("<b>Response:</b> " + response)

    def get_response(self, message):
        if message.lower() == "hello":
            return "Hello! How can I assist you?"
        else:
            return "I'm sorry, I don't understand that."
        
    def attach_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Attach File", "", "All Files (*);;Images (*.png *.jpg *.bmp)", options=options)
        if file_name:
            self.add_message(f"Attached: {file_name}", "User")

def main():
    app = QApplication(sys.argv)
    chat_app = ChatApplication()
    chat_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
