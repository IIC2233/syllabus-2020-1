from os import path
import json

def traducir_modulos(modulos_string):
    # Completar
    pass


def cargar_cursos(semestre):
    # Completar
    pass


if __name__ == "__main__":

    horario_ejemplo_1 = "AYU#M:4;CLAS#J:4,5;LAB;PRA;TAL;TER;TES"
    print(traducir_modulos(horario_ejemplo_1))
    horario_ejemplo_2 = "AYU;CLAS#L,W,V:3;LAB;LIB;PRA;SUP;TAL;TER;TES"
    print(traducir_modulos(horario_ejemplo_2))

    semestre = "2020-1" # Cambiar para probar

    cursos = cargar_cursos(semestre)

    with open("resultado_cargado.json", "wt", encoding="utf-8") as archivo:
        json.dump(cursos, archivo, indent=4)
