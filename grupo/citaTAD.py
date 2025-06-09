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
from datetime import datetime

def crearCita():
    #crea una cita vacía
    cita = ["", "", "", "", None, None]
    return cita

def cargarCita(cita, dni, nom, obraSoc, tel, fec, hor):
    #carga una nueva cita
    #[dni, nombre, obraSocial, telefono, fecha, hora]
    modDNI(cita, dni)
    modNombre(cita, nom)
    modObraSocial(cita, obraSoc)
    modTelefono(cita, tel)
    modFecha(cita, fec)
    modHora(cita, hor)

def asignarCita(cita1, cita2):
    #copia los datos de cita1 a cita2
    modDNI(cita2, verDNI(cita1))
    modNombre(cita2, verNombre(cita1))
    modObraSocial(cita2, verObraSocial(cita1))
    modTelefono(cita2, verTelefono(cita1))
    modFecha(cita2, verFecha(cita1))
    modHora(cita2, verHora(cita1))

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
    #Retorna la fecha de la cita en formato DD/MM/AAAA
    fecha = cita[4]
    return fecha.strftime("%d/%m/%Y") if fecha else ""

def verHora(cita):
    #Retorna la hora de la cita en formato HH:MM
    hora = cita[5]
    return hora.strftime("%H:%M") if hora else ""

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
    if nuevaFecha:
        cita[4] = datetime.strptime(nuevaFecha, "%d/%m/%Y")
    else:
        cita[4] = None

def modHora(cita, nuevaHora):
    #Modifica la hora de la cita
    if nuevaHora:
        hora_obj = datetime.strptime(nuevaHora, "%H:%M").time()
        cita[5] = hora_obj
    else:
        cita[5] = None