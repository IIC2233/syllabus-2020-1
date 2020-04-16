import os

from cargar_datos import (
    cargar_clave_unica, cargar_permiso_hora, cargar_datos,
    cargar_permiso_supermercado, cargar_comunas_en_cuarentena
)

from permisos import (
    verificar_rut, permiso_clave_unica,
    permiso_asistencia_medica, permiso_servicios_basicos
)

# Debes completar esta clase
class ErrorPermiso(Exception):

    def __init__(self, opcion, dic_opciones):
        super().__init__()
        pass

    def mostrar_opciones_validas(self):
        pass


if __name__ == "__main__":

    comunas_cuarentena = cargar_comunas_en_cuarentena(os.path.join("datos", 'cuarentena.csv')) #lista de comunas
    datos_clave_unica = cargar_clave_unica(os.path.join("datos", 'ruts_clave_unica.csv')) #lista de ruts
    datos_registrados = cargar_datos(os.path.join("datos", 'datos.csv')) #dict de namedtuples
    datos_horas = cargar_permiso_hora(os.path.join("datos", 'permiso_hora.csv')) #dict de namedtuples
    datos_permiso_supermercado = cargar_permiso_supermercado(os.path.join("datos", 'permiso_supermercado.csv')) #dict de namedtuples

    def clave_unica(datos_clave_unica, datos_registrados):
        for rut in datos_clave_unica:
            try:
                verificar_rut(rut, datos_registrados)
                permiso_clave_unica(rut, datos_registrados)
                print("Clave única obtenida con éxito")

            #Tienes que implementar las excepciones
            except:
                pass

    def asistencia_medica(datos_horas, datos_registrados):
        for solicitud in datos_horas.values():
            try:
                verificar_rut(solicitud.rut, datos_registrados)
                permiso_asistencia_medica(solicitud.hora)
                print("Permiso de Servicio de asistencia médica obtenido con éxito")

            #Tienes que implementar las excepciones
            except:
                pass

    def asistencia_servicios_basicos(datos_permiso_supermercado, datos_registrados, comunas_cuarentena):
        for solicitud in datos_permiso_supermercado.values():
            try:
                persona = verificar_rut(solicitud.rut, datos_registrados)
                permiso_servicios_basicos(persona, solicitud, comunas_cuarentena)
                print("Permiso de Servicios básicos obtenido con éxito")

            # Tienes que implementar esta excepción
            except:
                pass


    dic_opciones = {
        "1" : "Permisos de Clave Unica",
        "2" : "Permisos de Asistencia Médica",
        "3" : "Permisos de Servicios Básicos",
        "0" : "Salir"
    }

    continuar = True
    while continuar:

        print("\n Menu DCComisaria Virtual")

        for key, value in dic_opciones.items():
            print(f"[{key}] {value}")

        opcion = input("Ingresa el permiso que deseas realizar: ")

        try:
            if opcion in dic_opciones.keys():
                permiso = dic_opciones[opcion]

                if permiso ==  "Permisos de Clave Unica":
                    clave_unica(datos_clave_unica, datos_registrados)

                elif permiso == "Permisos de Asistencia Médica":
                    asistencia_medica(datos_horas, datos_registrados)

                elif permiso == "Permisos de Servicios Básicos":
                    asistencia_servicios_basicos(datos_permiso_supermercado, datos_registrados, comunas_cuarentena)

                elif permiso == "Salir":
                    continuar = False

            else:
                raise ErrorPermiso(opcion, dic_opciones)

        except:
            pass
