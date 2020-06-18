class Pixel:
    """
    Objeto Pixel del server, almacena el estado de un pixel dentro del canvas
    Atributos:
        - x_pos        : int, contiene la posición x del pixel en el canvas
        - y_pos        : int, contiene la posición x del pixel en el canvas
        - nombre_color : string, describe el color del pixel
    """
    def __init__(self, x_pos, y_pos, nombre_color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.nombre_color = nombre_color


class Canvas:
    """
    Objeto Canvas del server, almacena objetos Pixel y los administra
    Atributos:
        - columnas : int, contiene el número de columnas (x) del canvas
        - filas    : int, contiene el número de filas (y) del canvas
        - pixeles  : list of lists of pixeles, contiene los objetos Pixel
    """
    def __init__(self, columnas, filas):
        self.columnas = columnas
        self.filas = filas
        self.pixeles = []
        for fila in range(self.columnas):
            fila_pixeles = []
            for columna in range(self.filas):
                # Blanco es el color por defecto
                pixel = Pixel(columna, fila, "white")
                fila_pixeles.append(pixel)
            self.pixeles.append(fila_pixeles)

    def obtener_tablero(self):
        """
        Genera un diccionario a partir de los contenidos de pixeles.
        El diccionario es de la forma { fila : { columna : color } }. Ejemplo:
        {
            "0" : {
                "0" : "white",
                "1" : "black",
                "2" : "white",
                "3" : "red",
                ...
            },
            "1" : {
                "0" : "white",
                ...
            }
            ...
        }
        Retorna dicho diccionario
        """
        dict_ = dict()
        for fila in range(self.filas):
            dict_[str(fila)] = dict()
            for columnas in range(self.columnas):
                dict_[str(fila)][str(columnas)] = self.pixeles[fila][columnas].nombre_color
        return dict_

    def pintar_pixel(self, dict_):
        """
        Cambia el color del pixel en x_pos, y_pos
        Argumentos:
            - dict_ : Diccionario que contiene información del cambio.
                      Posee los siguientes valores:
                      - x_pos        : int
                      - y_pos        : int
                      - nombre_color : string, contiene el nuevo color del pixel
        """
        x_pos = int(dict_["x_pos"])
        y_pos = int(dict_["y_pos"])
        nombre_color = dict_["nombre_color"]
        if x_pos < self.columnas and y_pos < self.filas:
            self.pixeles[y_pos][x_pos].nombre_color = nombre_color
        else:
            print(f"Error! Se intentó pintar el pixel ({x_pos}, {y_pos}), que no existe!")
