import sys
import socket
from servidor import Servidor


if __name__ == "__main__":
    HOST = socket.gethostname()
    PORT = 45743

    try:
        SERVIDOR = Servidor(HOST, PORT)
        # Esto permite cerrar el server con Ctrl+C
        while True:
            input("CTRL + C -> SALIR\n")
    except KeyboardInterrupt:
        SERVIDOR.socket_server.close()
        print("Forzando cierre de servidor!")
        sys.exit(0)
