import json
import pickle

from cargar_cursos import cargar_cursos, traducir_modulos
from consultas import (
    filtrar_por, filtrar_por_cupos, filtrar_por_modulos,
    filtrar_por_prerrequisitos, filtrar_por_cursos_compatibles
)


class Test:

    def __init__(self, argumentos, output_esperado, funcion):
        # La cantidad de argumentos debe coincidir con la cantidad de outputs
        if len(argumentos) != len(output_esperado):
            raise ValueError("Tamaño de input no coincide con tamaño de output")
        # Los argumentos deben ser una lista de tuplas
        if not all(isinstance(args, tuple) for args in argumentos):
            raise TypeError("Argumentos debe ser una lista de tuplas")
        # Los outputs deben ser objetos serializables a JSON
        # (esto ya que siempre se trabaja con diccionario como output)
        for output in output_esperado:
            try:
                json.dumps(output)
            except:
                raise ValueError("Todo output esperado debe ser serializable a JSON")
        self.argumentos = argumentos
        self.output_esperado = output_esperado
        # Funcion debe ser "llamable", para poder darle los argumentos
        if not callable(funcion):
            raise TypeError("Funcion debe ser llamable (usa solo el nombre)")
        self.funcion = funcion
        self.resultados = []

    def probar_casos(self):
        print(f"Tests para función: {self.funcion.__name__}.\n")
        self.resultados = []
        for i, (args, output_esperado) in enumerate(zip(self.argumentos, self.output_esperado)):
            try:
                # Intentamos ejecutar la función a testear para obtener respuesta
                respuesta = self.funcion(*args)
            except Exception as e:
                # En caso de error, se imprime y salta al siguiente test
                print(f"Error al ejecutar función en test #{i}: {e}\n")
                self.resultados.append(None)
                continue
            try:
                # Se compara el resultado con el output esperado en otro método
                correcto = self.comparar(respuesta, output_esperado)
                if correcto:
                    mensaje = f"Respuestas en test #{i} coinciden"
                else:
                    mensaje = f"ERROR: no coinciden respuestas en test #{i}"
                print(mensaje)
            except Exception as e:
                # En caso de error al comparar, se imprime y la respuesta es incorrecta
                print(f"Error al comparar respuestas en test #{i}: {e}")
                correcto = False
            finally:
                # Se guarda el resultado
                self.resultados.append(correcto)
                print()
        # Se imprimen resultados importantes
        print(f"Casos probados: {len(self.argumentos)}")
        print(f"Correctos: {sum(1 if r is True else 0 for r in self.resultados)}")
        print(f"Incorrectos: {sum(1 if r is False else 0 for r in self.resultados)}")
        print(f"Errores: {sum(1 if r is None else 0 for r in self.resultados)}")

    def comparar(self, respuesta, output_esperado):
        if isinstance(respuesta, dict) and isinstance(output_esperado, dict):
            if not self.comparar(sorted(respuesta.keys()), sorted(output_esperado.keys())):
                return False
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
            if len(respuesta) != len(output_esperado):
                return False
            return all(self.comparar(respuesta[i], output_esperado[i]) for i in range(len(respuesta)))
        return respuesta == output_esperado


if __name__ == "__main__":

    # Ejemplo: Testeando "traducir_modulos"
    # El primer test debería provocar un error en la función testeada,
    # pero es solo para mostrar que el test es resistente a errores.

    # Argumentos debe ser una lista de tuplas
    # Cada tupla son los argumentos que se le entregan a la función a testear
    argumentos = [
        (None,),  # Se espera que falle
        ("CLAS;TES;LAB;TER;PRA;AYU;TAL",),  # (0) Sin modulos
        ("AYU;CLAS#V:3;TES;TAL;LAB;PRA;TER",),  # (1) Un módulo, un día
        ("PRA#J,V:2;TER;TES;AYU;CLAS;TAL;LAB",),  # (2) Un módulo, dos días
        ("TES;AYU;CLAS;PRA;LAB#M,J:7;TAL;TER#L,M:2",),  # (2b) Un módulo, dos días (múltiples veces)
        ("LAB;PRA;TER;TAL;TES#L,W,V:1;AYU;CLAS",),  # (3) Un módulo, tres dias
        ("TAL;AYU#L:5,6;CLAS;TES;PRA;LAB;TER",),  # (4) Dos módulos, un dia
        ("TES;LAB;TAL;TER;PRA;AYU;CLAS#V:5,6,7",),  # (5) Tres módulos, un dia
        ("AYU#W,J:7,8;PRA;CLAS;LAB;TER;TES;TAL",),  # (6) Dos módulos, dos dias
        ("TES#M,J:3,4;LAB;TER;AYU;PRA;CLAS#M,J:1,2;TAL",),  # (6b) Dos módulos, dos dias (múltiples veces)
        ("PRA;TES;TAL#M,W,J:3,4,5;AYU;LAB;TER#M,W,J:3,4,5;CLAS",),  # (7) Tres módulos, Tres dias
    ]
    # Output esperado debe ser una lista de objetos
    # Cada objeto será comparado con el resultado obtenido para los argumentos correspondientes
    output_esperado = [
        {},
        {"TES": [], "CLAS": [], "LAB": [], "TER": [], "PRA": [], "AYU": [], "TAL": []},
        {"AYU": [], "CLAS": [("V", 3)], "TES": [], "TAL": [], "LAB": [], "PRA": [], "TER": []},
        {"PRA": [("J", 2), ("V", 2)], "TER": [], "TES": [], "AYU": [], "CLAS": [], "TAL": [], "LAB": []},
        {"TES": [], "AYU": [], "CLAS": [], "PRA": [], "LAB": [("M", 7), ("J", 7)], "TAL": [], "TER": [("L", 2), ("M", 2)]},
        {"LAB": [], "PRA": [], "TER": [], "TAL": [], "TES": [("L", 1), ("W", 1), ("V", 1)], "AYU": [], "CLAS": []},
        {"TAL": [], "AYU": [("L", 5), ("L", 6)], "CLAS": [], "TES": [], "PRA": [], "LAB": [], "TER": []},
        {"TES": [], "LAB": [], "TAL": [], "TER": [], "PRA": [], "AYU": [], "CLAS": [("V", 5), ("V", 6), ("V", 7)]},
        {"AYU": [("W", 7), ("W", 8), ("J", 7), ("J", 8)], "PRA": [], "CLAS": [], "LAB": [], "TER": [], "TES": [], "TAL": []},
        {"TES": [("M", 3), ("M", 4), ("J", 3), ("J", 4)], "LAB": [], "TER": [], "AYU": [], "PRA": [], "CLAS": [("M", 1), ("M", 2), ("J", 1), ("J", 2)], "TAL": []},
        {"PRA": [], "TES": [], "TAL": [("M", 3), ("M", 4), ("M", 5), ("W", 3), ("W", 4), ("W", 5), ("J", 3), ("J", 4), ("J", 5)], "AYU": [], "LAB": [], "TER": [("M", 3), ("M", 4), ("M", 5), ("W", 3), ("W", 4), ("W", 5), ("J", 3), ("J", 4), ("J", 5)], "CLAS": []},
    ]
    # Se instancia el contenedor de test y se prueban los casos
    test_traducir_modulos = Test(argumentos, output_esperado, traducir_modulos)
    test_traducir_modulos.probar_casos()


    # Aquí se simulará el diccionario de cursos con esta versión que solo contiene
    # a Programación Avanzada (este curso). Se utiliza pickle ya que al serializar
    # en JSON, las listas y tuplas se convierten al mismo tipo (arreglo)
    with open("cursos.test", "rb") as f:
        # dicc_cursos = { "IIC2233": ... }
        dicc_cursos = pickle.load(f)

    # Ejemplo: Testeando "filtrar_por"
    # En este test, efectivamente se espera que solo se retorne la sección donde
    # el profesor es 'CRIStian ruz'.
    argumentos = [
        ("Profesor", "cris", dicc_cursos)
    ]
    output_esperado = [
        {
            "IIC2233": {
                "Nombre": "Programación Avanzada",
                "Retiro": "SI",
                "Aprobacion Especial": "NO",
                "Creditos": 10,
                "Ingles": "NO",
                "Sigla": "IIC2233",
                "Prerrequisitos": ["IIC1103", "IIC1102"],
                "Secciones": {
                    "1": {
                        "Campus": "San Joaquín",
                        "Formato": "Presencial",
                        "Modulos": {"AYU": [("M", 4)], "CLAS": [("J", 4), ("J", 5)], "LAB": [], "PRA": [], "TAL": [], "TER": [], "TES": []},
                        "NRC": "12431",
                        "Profesor": "Ruz Cristian",
                        "Seccion": "1",
                        "Semestre": "2019-2",
                        "Vacantes disponibles": 12,
                        "Vacantes totales": 110,
                    },
                },
            }
        },
    ]
    # Se instancia el contenedor de test y se prueban los casos
    test_filtrar_por = Test(argumentos, output_esperado, filtrar_por)
    test_filtrar_por.probar_casos()
