import sys
import socket
from PyQt5.QtWidgets import QApplication
from cliente import Cliente


if __name__ == "__main__":
    # Se inicia la interfaz.
    app = QApplication([])

    # Se estableces el host y port.
    # Puedes modificar estos valores si lo deseas.
    HOST = socket.gethostname()
    PORT = 45743

    # Se intancia el Cliente.
    CLIENTE = Cliente(HOST, PORT)

    # Se inicia la app de PyQt.
    sys.exit(app.exec_())
