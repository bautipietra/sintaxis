import pyfiglet
from libreriaTAD import *
from libroTAD import *

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

libreria = crearLibreria()

def seleccionarOpcion():
  option = int(input("\n Seleccione una opción (1-6): "))

  if (option == 1):
    print(bcolors.OKBLUE + "\n Ingrese los datos para crear el libro \n")
    libro = crearLibro()
    titulo = input("Ingrese el titulo: ")
    autor = input("Ingrese el autor: ")
    editorial = input("Ingrese la editorial: ")
    precio = input("Ingrese el precio: ")
    cargarLibro(libro, titulo, autor, editorial, precio)
    agregarLibro(libreria, libro)
  elif (option == 2):
    print(obtenerTodosLosLibros(libreria))
  elif (option == 3):
    indice = int(input("\nIngrese un indice: "))
    print(obtenerLibro(libreria, indice))
  elif (option == 4):
    editorial = input("\nIngrese una editorial: ")
    print(obtenerLibrosPorEditorial(libreria, editorial))
  elif (option == 5):
    i = int(input("\nIngrese el indice del libro que desea modificar: "))
    print(obtenerLibro(libreria, i))
    print("\n¿Que propiedad desea modificar?: ")
    print("1. Titulo")
    print("2. Autor")
    print("3. Editorial")
    print("4. Precio")
    op = int(input("\nSeleccione una opción (1-4): "))
    if (op == 1):
      titulo = input("\nIngrese el nuevo titulo: ")
      modificarTitulo(obtenerLibro(libreria, i), titulo)
    elif (op == 2):
      autor = input("\nIngrese el nuevo autor: ")
      modificarAutor(obtenerLibro(libreria, i), autor)
    elif (op == 3):
      editorial = input("\nIngrese la nueva editorial: ")
      modificarEditorial(obtenerLibro(libreria, i), editorial)
    elif (op == 4):
      precio = input("\nIngrese el nuevo precio: ")
      modificarPrecio(obtenerLibro(libreria, i), precio)
  elif (option == 6):
    i = int(input("\nIngrese el indice del libro que desea eliminar: "))
    eliminarLibro(libreria, obtenerLibro(libreria, i))
  elif (option == 7):
    print("\nGracias por usar nuestra aplicación, ¡nos vemos pronto!")
    print("Saliendo...")
    return

  input("\nPresiona enter para volver al menu principal\n")  
  menu()

def menu():
  print(pyfiglet.figlet_format("App de Librerias"))
  print("1. Crear libro")
  print("2. Mostrar libros")
  print("3. Mostrar libro por indice")
  print("4. Mostrar libros por editorial")
  print("5. Modificar libro")
  print("6. Eliminar libro")
  print("7. Salir")
  seleccionarOpcion()

menu()