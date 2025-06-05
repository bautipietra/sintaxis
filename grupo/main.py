import pyfiglet
from agendaTAD import *
from citaTAD import *
from colaTAD import *

# Crear textos de colores
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
    
def obtenerTodasLasCitas(agenda):
    #retorna todas las citas de la agenda
    citas = []
    for i in range(tamanioAgenda(agenda)):
        cita = obtenerCita(agenda, i)
        citas.append(cita)
    return citas

def mostrarCola(cola):
    #imprime la cola
    print("\n")
    print("Cola:")
    for i in range(tamanio(cola)):
        print(desencolar(cola))

agenda = crearAgenda()

def seleccionarOpcion():
    option = int(input("\nSeleccione una opción (1-11): "))

    if (option == 1):
        print(bcolors.OKBLUE + "\nIngrese los datos para crear la cita\n")
        cita = crearCita()
        dni = input("Ingrese el DNI del paciente: ")
        nombre = input("Ingrese el nombre del paciente: ")
        obraSocial = input("Ingrese la obra social: ")
        telefono = input("Ingrese el teléfono: ")
        fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
        hora = input("Ingrese la hora (HH:MM): ")
        cargarCita(cita, dni, nombre, obraSocial, telefono, fecha, hora)
        agregarCita(agenda, cita)
        print(bcolors.OKGREEN + "\n¡Cita agregada exitosamente!" + bcolors.ENDC)

    elif (option == 2):
        print(bcolors.OKBLUE + "\nCitas en la agenda:" + bcolors.ENDC)
        obtenerTodasLasCitas(agenda)
        recorrerCitas(agenda)

    elif (option == 3):
        indice = int(input("\nIngrese el índice de la cita: "))
        if indice > tamanioAgenda(agenda):
            print(bcolors.FAIL + "No se encontró una cita en esa posición" + bcolors.ENDC)
        else:
            cita = obtenerCita(agenda, indice)
            if isinstance(cita, str):
                print(bcolors.FAIL + cita + bcolors.ENDC)
            else:
                print(bcolors.OKBLUE + "\nDatos de la cita:" + bcolors.ENDC)
                mostrarCita(cita)

    elif (option == 4):
        fecha = input("\nIngrese la fecha a buscar (DD/MM/AAAA): ")
        citas = obtenerTodasLasCitas(agenda)
        citasFecha = []
        print(bcolors.OKBLUE + f"\nCitas para el {fecha}:" + bcolors.ENDC)
        for i in range(tamanioAgenda(agenda)):
            cita = obtenerCita(agenda, i)
            if verFecha(cita) == fecha:
                mostrarCita(cita)
        if not citasFecha:
            print("No hay citas para esa fecha")

    elif (option == 5):
        i = int(input("\nIngrese el índice de la cita a modificar: "))
        cita = obtenerCita(agenda, i)
        if isinstance(cita, str):
            print(bcolors.FAIL + cita + bcolors.ENDC)
        else:
            print("\n¿Qué propiedad desea modificar?:")
            print("1. DNI")
            print("2. Nombre")
            print("3. Obra Social")
            print("4. Teléfono")
            print("5. Fecha")
            print("6. Hora")
            op = int(input("\nSeleccione una opción (1-6): "))
            
            if op == 1:
                nuevoDNI = input("\nIngrese el nuevo DNI: ")
                modDNI(cita, nuevoDNI)
            elif op == 2:
                nuevoNombre = input("\nIngrese el nuevo nombre: ")
                modNombre(cita, nuevoNombre)
            elif op == 3:
                nuevaObraSocial = input("\nIngrese la nueva obra social: ")
                modObraSocial(cita, nuevaObraSocial)
            elif op == 4:
                nuevoTelefono = input("\nIngrese el nuevo teléfono: ")
                modTelefono(cita, nuevoTelefono)
            elif op == 5:
                nuevaFecha = input("\nIngrese la nueva fecha (DD/MM/AAAA): ")
                modFecha(cita, nuevaFecha)
            elif op == 6:
                nuevaHora = input("\nIngrese la nueva hora (HH:MM): ")
                modHora(cita, nuevaHora)
            print(bcolors.OKGREEN + "\n¡Cita modificada exitosamente!" + bcolors.ENDC)

    elif (option == 6):
        i = int(input("\nIngrese el índice de la cita a eliminar: "))
        cita = obtenerCita(agenda, i)
        if isinstance(cita, str):
            print(bcolors.FAIL + cita + bcolors.ENDC)
        else:
            mostrarCita(cita)
            eliminarCita(agenda, cita)
            print(bcolors.OKGREEN + "\n¡Cita eliminada exitosamente!" + bcolors.ENDC)

    elif (option == 7):
        dni = input("\nModificar cita por el DNI del paciente: ")
        for i in range(tamanioAgenda(agenda)):
            cita = obtenerCita(agenda, i)
            if verDNI(cita) == dni:
                nuevaFecha = input("\nIngrese la nueva fecha (DD/MM/AAAA): ")
                modFecha(cita, nuevaFecha)
                nuevaHora = input("\nIngrese la nueva hora (HH:MM): ")
                modHora(cita, nuevaHora)
                print(bcolors.OKGREEN + "\n¡Cita modificada exitosamente!" + bcolors.ENDC)
                break
        else:
            print(bcolors.FAIL + "No se encontró una cita con ese DNI" + bcolors.ENDC)
       
    elif (option == 8):
        fecha = input("\nIngrese la fecha de las citas (DD/MM/AAAA): ")
        fechaNueva = input("\nIngrese la fecha nueva (DD/MM/AAAA): ")
        for i in range(tamanioAgenda(agenda)):
            cita = obtenerCita(agenda, i)
            if verFecha(cita) == fecha:
                modFecha(cita, fechaNueva)
        print(bcolors.OKGREEN + "\n¡Citas modificadas exitosamente!" + bcolors.ENDC)

    elif (option == 9):
        obra = input("\nIngrese la obra social: ")
        i = 0
        contador = 0
        while i < tamanioAgenda(agenda):
            cita = obtenerCita(agenda, i)
            if verObraSocial(cita) == obra:
                contador += 1
                mostrarCita(cita)
                eliminarCita(agenda, cita)
                print(bcolors.OKGREEN + "\n¡Cita eliminada exitosamente!" + bcolors.ENDC)
            i += 1
        if contador == 0:
            print(bcolors.FAIL + "No se encontró ninguna cita con esa obra social" + bcolors.ENDC)


    elif (option == 10):
        fecha = input("\nIngrese la fecha de las citas (DD/MM/AAAA): ")
        cola = crearCola()
        for i in range(tamanioAgenda(agenda)):
            cita = obtenerCita(agenda, i)
            if verFecha(cita) == fecha:
                encolar(cola, cita)
        mostrarCola(cola)

    elif (option == 11):
        print(bcolors.OKGREEN + "\nGracias por usar nuestra aplicación, ¡nos vemos pronto!" + bcolors.ENDC)
        print("Saliendo...")
        return

    input("\nPresiona enter para volver al menú principal\n")
    menu()

def menu():
    print(pyfiglet.figlet_format("Agenda Medica"))
    print("1. Crear cita")
    print("2. Mostrar todas las citas")
    print("3. Mostrar cita por índice")
    print("4. Mostrar citas por fecha")
    print("5. Modificar cita")
    print("6. Eliminar cita")
    print("7. Modificar cita por DNI")
    print("8. Mover todas las citas de una fecha a otra")
    print("9. Eliminar todas las citas de una obra social")
    print("10. Mostrar citas en cola por fecha")
    print("11. Salir")
    seleccionarOpcion()

menu()