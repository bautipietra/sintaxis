"""
TAD AGENDA

La agenda es una lista de citas
"""

agenda = []

def crearAgenda():
    #crea una agenda vacía
    agenda = []
    return agenda

def agregarCita(agenda, cita):
    #agrega una cita a la agenda
    agenda.append(cita)

def eliminarCita(agenda, cita):
    #elimina una cita de la agenda
    agenda.remove(cita)

def obtenerCita(agenda, i):
    #retorna la cita en la posición i
    if (i >= tamanioAgenda(agenda)):
        return "No se encontró una cita en esa posición"
    else:
        return agenda[i]

def obtenerTodasLasCitas(agenda):
    #retorna todas las citas de la agenda
    return agenda

def tamanioAgenda(agenda):
    #retorna la cantidad de citas en la agenda
    return len(agenda)

def existeCita(agenda, cita):
    #verifica si una cita existe en la agenda
    return cita in agenda

def obtenerCitasPorFecha(agenda, fecha):
    #retorna una lista con las citas de una fecha específica
    citasFecha = []
    for cita in agenda:
        if verFecha(cita) == fecha:
            citasFecha.append(cita)
    return citasFecha