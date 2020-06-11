import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import pyqtSignal


class VentanaPrincipal(QWidget):

    senal_enviar_info = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()

        # Parámetros de la ventana
        self.setGeometry(220, 120, 850, 350)
        self.setMaximumSize(850, 350)
        self.setMinimumSize(850, 350)
        self.setStyleSheet('background-color: #FFFFFF')
        self.setWindowTitle('Avanzada Quién?')

        # cartas base
        ruta_carta = os.path.join('sprites', 'carta.png')
        self.cartas = [QLabel(self), QLabel(self), QLabel(self), QLabel(self)]
        for i in range(len(self.cartas)):
            self.cartas[i].setPixmap(QPixmap(ruta_carta))
            self.cartas[i].setGeometry(10 + i * 210, 10, 200, 265)
        
        # Texto para usuario
        self.etiqueta = QLabel('Usuario:', self)
        self.etiqueta.setGeometry(310, 290, 200, 20)

        # Texto para contraseña
        self.etiqueta_contraseña = QLabel('Contraseña:', self)
        self.etiqueta_contraseña.setGeometry(290, 320, 200, 20)

        # Respuesta
        self.respuesta = QLabel('', self)
        self.respuesta.setGeometry(650, 300, 100, 20)

        # Formulario usuario
        self.usuario = QLineEdit('', self)
        self.usuario.setGeometry(360, 290, 130, 20)

        # Formulario contraseña
        self.clave = QLineEdit('', self)
        self.clave.setGeometry(360, 320, 130, 20)

        # botón
        self.boton = QPushButton('Ingresar', self)
        self.boton.setGeometry(530, 290, 80, 40)
        self.boton.setStyleSheet('background-color: #d5d4d3')
        self.boton.clicked.connect(self.enviar_input)


    def enviar_input(self):
        usuario = self.usuario.text()
        clave = self.clave.text()
        self.senal_enviar_info.emit(usuario, clave)
    
    def revelar(self, path, indice):
        if not path:
            if indice == 'usuario':
                self.respuesta.setText('¡Usuario incorrecto!')
            elif indice == 'clave':
                self.respuesta.setText('¡Clave incorrecta!')
        else:
            indice = int(indice)
            self.cartas[indice].setPixmap(QPixmap(path))
            self.respuesta.setText('¡Felicitaciones!')

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
