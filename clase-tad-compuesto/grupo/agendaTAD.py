"""
TAD AGENDA

La agenda es una lista de citas
"""
from agendaTAD import *

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

def eliminarCitaPorObraSocial(agenda, obra):
    #elimina todas las citas que correspondan a una obra social específica
    i = 0
    while i < len(agenda):
        if agenda[i][2] == obra:
            agenda.pop(i)
        else:
            i += 1
    return agenda

def obtenerCita(agenda, i):
    #retorna la cita en la posición i
    if (i > tamanioAgenda(agenda)):
        return "No se encontró una cita en esa posición"
    else:
        return agenda[i-1]

def obtenerCitaPorDNI(agenda, dni):
    #retorna la cita en la posición i
    for cita in agenda:
        if cita[0] == dni:
            print(cita)
            return cita
    return "No se encontró una cita con ese DNI"

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
        if cita[4] == fecha:
            citasFecha.append(cita)
    return citasFecha