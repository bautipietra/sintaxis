""" 
Generar una nueva cola que contenga únicamente los nombres y obras sociales de los pacientes citados en un día específico, e imprimirla inmediatamente en pantalla.
 """

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