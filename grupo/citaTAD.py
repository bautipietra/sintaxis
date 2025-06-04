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

def crearCita():
    #crea una cita vacía
    cita = ["", "", "", "", "", ""]
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

def mostrarCita(cita):
    #Muestra los datos de la cita
    print("\nDatos de la cita:")
    print(f"DNI: {verDNI(cita)}")
    print(f"Nombre: {verNombre(cita)}")
    print(f"Obra Social: {verObraSocial(cita)}")
    print(f"Teléfono: {verTelefono(cita)}")
    print(f"Fecha: {verFecha(cita)}")
    print(f"Hora: {verHora(cita)}")

def recorrerCitas(citas):
    #recorre todas las citas de la agenda
    for cita in citas:
        mostrarCita(cita)