import json
import os


def desencriptar(string):
    letras = list('arquetipos')
    numeros = list('0123456789')
    lista_string = list(string)
    for i in range(len(lista_string)):
        if lista_string[i] in letras:
            letra = lista_string.pop(i)
            lista_string.insert(i, numeros[letras.index(letra)])
        elif lista_string[i] in numeros:
            numero = lista_string.pop(i)
            lista_string.insert(i, letras[numeros.index(numero)])
    return ''.join(lista_string)


class AyudanteTareo:
    def __init__(self, usuario, cargo, pokemon, pizza, serie):
        self.usuario = usuario
        self.cargo = cargo
        self.pokemon = pokemon
        self.pizza = pizza
        self.serie = serie

    def __repr__(self):
        return (f'| {self.usuario:16s} | {self.cargo:13s} | {self.pokemon:10s} |'
            f' {self.pizza:12s} | {self.serie:19s} |')


def cargar_ayudantes(ruta):
    # Completa esta función
    pass


if __name__ == '__main__':
    print(f'| {"Usuario":16s} | {"Cargo":13s} | {"Pokemon":10s} | {"Pizza":12s} | {"Serie":19s} |')
    print('--------------------------------------------------------------------------------------')
    for ayudante in cargar_ayudantes(os.path.join('tareas.json')):
        print(ayudante)
