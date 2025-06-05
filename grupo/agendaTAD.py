"""
TAD AGENDA

La agenda es una lista de citas
"""

from citaTAD import *

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
        return agenda[i-1]

def tamanioAgenda(agenda):
    #retorna la cantidad de citas en la agenda
    return len(agenda)

def existeCita(agenda, cita):
    #verifica si una cita existe en la agenda
    return cita in agenda
