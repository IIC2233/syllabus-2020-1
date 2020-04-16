

def verificar_rut(rut, datos_registrados):
    if "." in rut or "-" not in rut:
        # Levanta el error correspondiente
        pass

    if rut in datos_registrados.keys():
        return datos_registrados[rut]
    return

def permiso_clave_unica(rut, datos_registrados):
    if rut not in datos_registrados.keys():
        # Levanta el error correspondiente
        pass


def permiso_asistencia_medica(hora):
    if not hora.isdigit():
        # Levanta el error correspondiente
        pass


def permiso_servicios_basicos(persona, solicitud, comunas_cuarentena):

    if ((solicitud.salida not in comunas_cuarentena) and
        (solicitud.llegada not in comunas_cuarentena)):
        # Levanta el error correspondiente
        pass

    elif solicitud.salida != persona.domicilio:
        # Levanta el error correspondiente
        pass


