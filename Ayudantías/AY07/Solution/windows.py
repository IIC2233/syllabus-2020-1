import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout,
QPlainTextEdit, QLineEdit)
from PyQt5.QtCore import QCoreApplication, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap


class MailWindow(QWidget):

    send_mail_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):

        self.setGeometry(500, 100, 900, 500)
        self.setWindowTitle('DCCorreo')

        self.logo = QLabel(self)
        #self.logo.setFixedSize(800, 150)
        #self.logo.setGeometry(50, 50, 100, 100)

        path_logo = os.path.join("Data", "logo.png")
        pixeles = QPixmap(path_logo)
        
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)

        self.sender = QLabel('De:', self)
        # self.sender.move(10, 15)
        self.edit_sender = QLineEdit('', self)

        self.receiver = QLabel('Para:', self)
        # self.receiver.move(10, 15)
        self.edit_receiver = QLineEdit('', self)
        # self.edit_receiver.setGeometry(75, 15, 100, 20)

        self.subject = QLabel('Asunto:', self)
        # self.subject.move(10, 45)
        self.edit_subject = QLineEdit('', self)
        # self.edit_subject.setGeometry(75, 45, 100, 20)

        self.content = QPlainTextEdit(self)
        # self.content.move(100, 250)
        # self.content.resize(800, 1000)

        self.notification = QLabel("", self)

        self.send_button = QPushButton('ENVIAR', self)

        vbox_left = QVBoxLayout()
        vbox_left.addWidget(self.sender)
        vbox_left.addWidget(self.receiver)
        vbox_left.addWidget(self.subject)

        vbox_right = QVBoxLayout()
        vbox_right.addWidget(self.edit_sender)
        vbox_right.addWidget(self.edit_receiver)
        vbox_right.addWidget(self.edit_subject)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox_left)
        hbox.addLayout(vbox_right)

        vbox_main = QVBoxLayout()
        
        vbox_main.addWidget(self.logo)
        vbox_main.addLayout(hbox)
        vbox_main.addWidget(self.content)
        vbox_main.addWidget(self.notification)
        vbox_main.addWidget(self.send_button)
        self.setLayout(vbox_main)

        self.send_button.clicked.connect(self.button_handler)

    def button_handler(self):
        data = {
            "from": self.edit_sender.text(),
            "to": self.edit_receiver.text(),
            "subject": self.edit_subject.text(),
            "content": self.content.toPlainText()
            }
        self.send_mail_signal.emit(data)

    def response_handler(self, data):
        self.notification.setText(data["notification"])
        if data["status"] > 200:
            self.notification.setStyleSheet("*{color: 'red'}")
        elif data["status"] == 200:
            self.notification.setStyleSheet("*{color: 'green'}")
            self.edit_receiver.setText("")
            self.edit_subject.setText("")
            self.content.setPlainText("")
