import copy
import json
import os
import pickle

from cargar_cursos import cargar_cursos, traducir_modulos
from consultas import (
    filtrar_por, filtrar_por_cupos, filtrar_por_modulos,
    filtrar_por_prerrequisitos, filtrar_por_cursos_compatibles
)

CARPETA_TESTS = os.path.join("tests")


def cargar_tests_para(funcion, carpeta_tests=CARPETA_TESTS):
    # Cargar arguments y output esperado desde carpeta
    ruta_tests = os.path.join(carpeta_tests, f"test_{funcion.__name__}.test")
    with open(ruta_tests, "rb") as f:
        # Se cargan argumentos y output esperado desde el archivo serializado
        argumentos, output_esperado = pickle.load(f)
    # Convertimos los argumentos a una lista de tuplas
    argumentos = list(map(tuple, argumentos))
    # Se instancia la clase que realizará los tests
    test_manager = Test(argumentos, output_esperado, funcion)
    # Se ejecutan los tests
    test_manager.probar_casos()
    return test_manager.resultados


class Test:

    def __init__(self, argumentos, output_esperado, funcion):
        # La cantidad de argumentos debe coincidir con la cantidad de outputs
        if len(argumentos) != len(output_esperado):
            raise ValueError("Tamaño de input no coincide con tamaño de output")
        # Los argumentos deben ser una lista de tuplas
        if not all(isinstance(args, tuple) for args in argumentos):
            raise TypeError("Argumentos debe ser una lista de tuplas")
        # Los outputs esperados deben ser objetos serializables a JSON
        # (esto ya que siempre se trabaja con diccionario como output)
        for output in output_esperado:
            try:
                json.dumps(output)
            except:
                raise ValueError("Todo output esperado debe ser serializable a JSON")
        # Funcion debe ser "llamable", para poder darle los argumentos
        if not callable(funcion):
            raise TypeError("Funcion debe ser llamable (usa solo el nombre)")
        # Se guardan los objetos recibidos como atributos
        self.argumentos = argumentos
        self.output_esperado = output_esperado
        self.funcion = funcion
        # En este atributo se almacenarán los resultados de cada test
        self.resultados = []

    def probar_casos(self):
        self.resultados = []
        print(f"Tests para función: {self.funcion.__name__}")
        for i, (args, output_esperado) in enumerate(zip(self.argumentos, self.output_esperado)):
            # Se copian los argumentos por si la función modifica alguno
            args = copy.deepcopy(args)
            try:
                # Intentamos ejecutar la función a testear para obtener respuesta
                respuesta = self.funcion(*args)
            except Exception as e:
                # En caso de error al probar la función, se imprime y guarda como None
                print(f"Test #{i}) Excepción al ejecutar test ({e})")
                self.resultados.append(None)
                # Se salta al siguiente test ya que no se puede comparar
                continue
            try:
                # Se compara el resultado con el output esperado en otro método
                correcto = self.comparar(respuesta, output_esperado)
                if correcto:
                    mensaje = f"Test #{i}) Respuestas correcta"
                else:
                    mensaje = f"Test #{i}) Respuesta incorrecta"
                print(mensaje)
            except Exception as e:
                # En caso de error al comparar, se imprime y guarda como False
                print(f"Test #{i}) Excepción al ejecutar test ({e})")
                correcto = False
            finally:
                # Se guarda el resultado
                self.resultados.append(correcto)
        print()

    def comparar(self, respuesta, output_esperado):
        if isinstance(respuesta, dict) and isinstance(output_esperado, dict):
            # Si son diciconarios se comparan las llaves primero
            if not self.comparar(sorted(respuesta.keys()), sorted(output_esperado.keys())):
                return False
            # Si las llaves coinciden, se comparan los valores 1 a 1
            return all(self.comparar(respuesta[k], output_esperado[k]) for k in respuesta)
        elif isinstance(respuesta, list) and isinstance(output_esperado, list):
            if len(respuesta) != len(output_esperado):
                return False
            # Quitamos None para ordenar sin problemas
            respuesta = [e for e in respuesta if e is not None]
            output_esperado = [e for e in output_esperado if e is not None]
            # Comparamos largo nuevamente
            if len(respuesta) != len(output_esperado):
                return False
            # En las listas ignoramos el orden
            return self.comparar(tuple(sorted(respuesta)), tuple(sorted(output_esperado)))
        elif isinstance(respuesta, tuple) and isinstance(output_esperado, tuple):
            # Si son tuplas, se compara el largo y los valores 1 a 1
            if len(respuesta) != len(output_esperado):
                return False
            return all(self.comparar(respuesta[i], output_esperado[i]) for i in range(len(respuesta)))
        return respuesta == output_esperado


if __name__ == '__main__':

    # Para correr los tests de una función particular, se pueden comentar las demás líneas
    resultados = [
        cargar_tests_para(traducir_modulos),
        cargar_tests_para(cargar_cursos),
        cargar_tests_para(filtrar_por, os.path.join(CARPETA_TESTS, "2020-1")),
        cargar_tests_para(filtrar_por_cupos, os.path.join(CARPETA_TESTS, "2020-1")),
        cargar_tests_para(filtrar_por_prerrequisitos, os.path.join(CARPETA_TESTS, "2019-2")),
        cargar_tests_para(filtrar_por_modulos, os.path.join(CARPETA_TESTS, "2019-2")),
        cargar_tests_para(filtrar_por_cursos_compatibles, os.path.join(CARPETA_TESTS, "2019-1")),
    ]

    # Separación para imprimir resultados finales
    print("=" * 10, "RESULTADOS FINALES", "=" * 10)

    PUNTOS = [
        (traducir_modulos, 1.0),
        (cargar_cursos, 2.0),
        (filtrar_por, 1.5),
        (filtrar_por_cupos, 1.0),
        (filtrar_por_prerrequisitos, 1.0),
        (filtrar_por_modulos, 1.5),
        (filtrar_por_cursos_compatibles, 2.0),
    ]

    print()
    print(f"| {'Nombre funcion':<30s} | {'%':^6s} | {'Puntos':<9s} | {'C':^3s} | {'I':^3s} | {'E':^3s} |")
    print(f"| {'-' * 30} | {'-' * 6} | {'-' * 9} | {'-' * 3} | {'-' * 3} | {'-' * 3} |")
    OBTENIDO = 0
    TOTAL = sum(item[1] for item in PUNTOS)
    for resultado_test, (funcion, puntos) in zip(resultados, PUNTOS):
        # Porcentaje de tests correctos
        porcentaje_correctos = 100 * sum(filter(None, resultado_test)) / len(resultado_test)
        # Cálculo de puntaje
        puntos_obtenidos = None
        if porcentaje_correctos == 100:
            puntos_obtenidos = 1 * puntos
        elif porcentaje_correctos >= 75:
            puntos_obtenidos = 0.5 * puntos
        else:
            puntos_obtenidos = 0 * puntos
        # Conteo de resultados obtenidos
        C = sum(1 if r is True else 0 for r in resultado_test)  # Número de tests correctos
        I = sum(1 if r is False else 0 for r in resultado_test)  # Número de tests incorrectos
        E = sum(1 if r is None else 0 for r in resultado_test)  # Número de tests que lanzaron excepción
        # Imprimir de resultados para test
        print(
            f"| {funcion.__name__:<30s} | {porcentaje_correctos:5.1f}% | {puntos_obtenidos:.2f}/{puntos:.2f} "
            f"| {C:3} | {I:3} | {E:3} |"
        )
        # Acumular puntaje obtenido
        OBTENIDO += puntos_obtenidos

    print()
    print(f"Puntuación total: {OBTENIDO:.2f}/{TOTAL:.1f}")
