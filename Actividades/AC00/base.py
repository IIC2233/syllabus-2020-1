# Seccion para importar liberías

class Cuadrado(object):
    def __init__(self, arg):
        self.lado = arg
        self.angulo = 90

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado

class Triangulo(object):
    """
    Se supone un triángulo equilátero de lado = arg
    """
    def __init__(self, arg):
        self.lado = arg
        self.base = self.lado
        self.altura = self.lado * (3**(1/2)) / 2
        self.angulo = 60

    def area(self):
        return self.base * self.altura / 2

    def perimetro(self):
        return 3 * self.lado

if __name__ == '__main__':
    # Crear instancias aquí
    cuadrado = Cuadrado(2)
    triangulo = Triangulo(2)
