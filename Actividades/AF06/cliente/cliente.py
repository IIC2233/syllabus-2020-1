import sys
import threading
import json
import socket
from PyQt5.QtCore import pyqtSignal, QObject
from draw_color_canvas import VentanaPrincipal


class Cliente(QObject):

    senal_a_interfaz = pyqtSignal(dict)

    def __init__(self, host, port):
        super().__init__()

        # Se instancia la interfaz y se conectan las señales
        self.ventana_principal = VentanaPrincipal()
        self.ventana_principal.senal_a_cliente.connect(self.enviar_a_servidor)
        self.senal_a_interfaz.connect(self.ventana_principal.recibir_senal)

        # Se establece el IP y el puerto
        self.host = host
        self.port = port

        # Se crea el socket con protocolos IPv4, TCP.
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Se intenta conectar el socket con el servidor.
            self.socket_cliente.connect((self.host, self.port))

            self.conectado = True

            # Se inicia el método para escuchar información del servidor
            # con un thread, esto es para poder utilizar una interfaz en
            # paraleleo.
            self.thread_escuchar = threading.Thread(
                target=self.escuchar_servidor,
                daemon=True,
            )
            self.thread_escuchar.start()
        except ConnectionRefusedError:
            # En caso de error se informa al usuario y se termina el programa.
            print(f"ERROR: No se pudo conectar a {self.host}")
            self.socket_cliente.close()
            sys.exit()

        # Se inicia la interfaz, esté metodo de VentanaPrincipal fue
        # sobre-escrito para avisar al servidor que se ha conectado el
        # cliente con el comando "nuevo". (Linea 117 de draw_color_canvas.py)
        self.ventana_principal.show()

    def escuchar_servidor(self):
        """
        Permite que el cliente escuche los mensajes del servidor.
        """
        try:
            # =========================== COMPLETAR ===========================

            pass

            # =================================================================
        except (ConnectionResetError, json.JSONDecodeError):
            # En caso de un error en la conexión se informa y se cierra la
            # interfaz llamando al método closeEvent de VentanaPrincipal.
            # Línea 125 de draw_color_canvas.py
            print("¡Se perdió la conexión al servidor!")
            self.ventana_principal.closeEvent(None)
        finally:
            # Por último siempre se cierra el socket antes de terminar.
            self.socket_cliente.close()

    def enviar(self, mensaje):
        """
        Recibe un diccionario (mensaje).
        El diccionario debe ser codificado y enviado al servidor.
        """
        # ============================== COMPLETAR ============================

        pass

        # =====================================================================

    def enviar_a_servidor(self, dict_):
        """
        Permite separar las funciones de back-end y cliente, para enviar un
        diccionario desde la interfaz al servidor mediante señales y el método
        enviar.

        En caso de que este diccionario (dict_) contenga el comando "cerrar",
        se establece que el atributo self.conectado = False, es decir,
        se terminó la conexión desde closeEvent.
        """
        if dict_["comando"] == "cerrar":
            self.conectado = False

        self.enviar(dict_)
