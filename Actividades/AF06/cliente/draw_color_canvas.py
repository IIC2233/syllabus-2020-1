import sys
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPaintEvent, QPainter
from PyQt5.QtWidgets import (QPushButton, QLabel, QApplication, QWidget)


AVAILABLE_COLORS = {
    "white"   : Qt.white,
    "black"   : Qt.black,
    "red"     : Qt.red,
    "green"   : Qt.green,
    "yellow"  : Qt.yellow,
    "blue"    : Qt.blue,
    "cyan"    : Qt.cyan,
    "magenta" : Qt.magenta,
}


class Pixel(QWidget):
    def __init__(self, parent, x_pos, y_pos, color="white"):
        super().__init__(parent=parent)
        self.nombre_color = color
        self.color = AVAILABLE_COLORS[color]
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.setFixedSize(
            self.parent().tamano_pixel,
            self.parent().tamano_pixel
            )

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), self.color)

    def mouseReleaseEvent(self, event):
        dict_ = {
            "comando"      : "pintar",
            "x_pos"        : str(self.x_pos),
            "y_pos"        : str(self.y_pos),
            "nombre_color" : self.parent().color_actual
        }
        self.parent().senal_a_cliente.emit(dict_)


class ColorSelector(QWidget):
    def __init__(self, parent, color):
        super().__init__(parent=parent)
        self.nombre_color = color
        self.color = AVAILABLE_COLORS[color]
        self.setFixedSize(
            self.parent().tamano_pixel*2,
            self.parent().tamano_pixel*2
            )

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), self.color)

    def mouseReleaseEvent(self, event):
        self.parent().color_actual = self.nombre_color


class VentanaPrincipal(QWidget):

    senal_a_cliente = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        self.borde = 100  # Márgenes
        self.ancho_pixel = 50  # Numero de pixeles en una fila
        self.alto_pixel = 50  # Numero de pixeles en una columna
        self.tamano_pixel = 10
        self.color_actual = "yellow"
        self.move(300, 150)
        self.setFixedSize(700, 700)
        self.setWindowTitle("DrawColorCanvas")

        # Create canvas
        self.pixeles = []
        for fila in range(self.ancho_pixel):
            pixel_fila = []
            for columna in range(self.alto_pixel):
                pixel = Pixel(self, columna, fila, "white")
                pixel.move(self.borde + fila*self.tamano_pixel,
                           self.borde + columna*self.tamano_pixel)
                pixel_fila.append(pixel)
            self.pixeles.append(pixel_fila)

        # Create color bar
        self.label_barra = QLabel("Elige un color:", self)
        self.label_barra.move(
            self.borde,
            self.borde + self.alto_pixel*self.tamano_pixel + 20
            )

        self.barra_color = []
        for index, color in enumerate(AVAILABLE_COLORS):
            color_selector = ColorSelector(self, color)
            color_selector.move(
                self.borde + index*20,
                self.borde + self.alto_pixel*self.tamano_pixel + 50
                )
            self.barra_color.append(color_selector)

    def recibir_senal(self, dict_):
        if not dict_.get("cerrar"):
            self.update_all_pixels(dict_)

    def update_all_pixels(self, dict_):
        for fila in range(self.ancho_pixel):
            for columna in range(self.alto_pixel):
                pixel = self.pixeles[fila][columna]
                pixel.color = AVAILABLE_COLORS[dict_[str(fila)][str(columna)]]
                pixel.update()

    def show(self, *args, **kwargs):
        # Se envía una señal al cliente y posteriormente al servidor avisando
        # que se acaba de conectar con el comando "nuevo".
        self.senal_a_cliente.emit({"comando": "nuevo"})

        # Se continúa mostrando la interfaz utilizando el método original.
        super().show(*args, **kwargs)

    def closeEvent(self, event):
        if event:
            # Solo cuando el evento es válido (se presiona la x de la ventana)
            # se envía una señal al servidor para cerrar la conexión.
            self.senal_a_cliente.emit({"comando": "cerrar"})

        # Se cierra la ventana.
        self.deleteLater()


# Test window
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
