""" 
Generar una nueva cola que contenga únicamente los nombres y obras sociales de los pacientes citados en un día específico, e imprimirla inmediatamente en pantalla.
 """

from agendaTAD import *
from citaTAD import *

def crearCola():
    #Crea una cola vacia
    return []
   
def esVacia(cola):
    #Retorna Verdadero si la cola no tiene elementos
    return len(cola) == 0

def encolar(cola, elem):
    #Agrega un elemento al final de la cola       
    cola.append(elem)

def encolarPorFecha(agenda,cola, fecha):
    citas = obtenerCitasPorFecha(agenda, fecha)
    for cita in citas:
        nombre = verNombre(cita)
        obra = verObraSocial(cita)
        encolar(cola, [nombre, obra])
    return cola

def desencolar(cola):
    #Retorna y elimina el primer elemento de la cola
    if not esVacia(cola):
        return cola.pop(0)
    return None

def tamanio(cola):
    #Retorna la cantidad de elementos de la cola
    return len(cola)

def copiarCola(cola1,cola2):
    #Copia los datos de una cola a otra
    for elem in cola1:
        encolar(cola2, elem)
    return cola2

def imprimirCola(cola):
    #Imprime los elementos de la cola
    for elem in cola:
        print("\nDatos de la cita:")
        print(f"Nombre: {elem[0]}")
        print(f"Obra Social: {elem[1]}")