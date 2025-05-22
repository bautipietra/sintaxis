"""
TAD CITA

Propiedades:
- DNI del paciente (índice 0)
- nombre (índice 1)
- obra social (índice 2)
- teléfono (índice 3)
- fecha (índice 4)
- hora (índice 5)
"""

cita = ["", "", "", "", "", ""]
    #dni, nombre, obraSocial, telefono, fecha, hora

def crearCita():
    #crea una cita vacía
    cita = ["", "", "", "", "", ""]
    return cita

def cargarCita(cita, dni, nom, obraSoc, tel, fec, hor):
    #carga una nueva cita
    #[dni, nombre, obraSocial, telefono, fecha, hora]
    cita[0] = dni
    cita[1] = nom
    cita[2] = obraSoc
    cita[3] = tel
    cita[4] = fec
    cita[5] = hor

def asignarCita(cita1, cita2):
    #copia los datos de cita1 a cita2
    cita2[0] = cita1[0]
    cita2[1] = cita1[1]
    cita2[2] = cita1[2]
    cita2[3] = cita1[3]
    cita2[4] = cita1[4]
    cita2[5] = cita1[5]

def verDNI(cita):
    #Retorna el DNI del paciente
    return cita[0]

def verNombre(cita):
    #Retorna el nombre del paciente
    return cita[1]

def verObraSocial(cita):
    #Retorna la obra social del paciente
    return cita[2]

def verTelefono(cita):
    #Retorna el teléfono del paciente
    return cita[3]

def verFecha(cita):
    #Retorna la fecha de la cita
    return cita[4]

def verHora(cita):
    #Retorna la hora de la cita
    return cita[5]

def modDNI(cita, nuevoDNI):
    #Modifica el DNI del paciente
    cita[0] = nuevoDNI

def modNombre(cita, nuevoNombre):
    #Modifica el nombre del paciente
    cita[1] = nuevoNombre

def modObraSocial(cita, nuevaObraSocial):
    #Modifica la obra social del paciente
    cita[2] = nuevaObraSocial

def modTelefono(cita, nuevoTelefono):
    #Modifica el teléfono del paciente
    cita[3] = nuevoTelefono

def modFecha(cita, nuevaFecha):
    #Modifica la fecha de la cita
    cita[4] = nuevaFecha


def modHora(cita, nuevaHora):
    #Modifica la hora de la cita
    cita[5] = nuevaHora

def modFechaMasivo(citas, fechaNueva):
    #Modifica todas las citas de una fecha especifica a otra.
    for cita in citas:
        cita[4] = fechaNueva
