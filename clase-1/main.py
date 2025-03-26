from tadEstudiante import *

nombre = input("Ingrese el nombre del estudiante:")
legajo = input("Ingrese el legajo del estudiante:")

estudiante = crearEstudiante()
cargarEstudiante(estudiante, nombre, legajo)

nota1 = int(input("Ingrese la primera nota:"))
nota2 = int(input("Ingrese la segunda nota:"))
nota3 = int(input("Ingrese la tercera nota:"))
agregarNota(estudiante, nota1)
agregarNota(estudiante, nota2)
agregarNota(estudiante, nota3)

print(promedio(estudiante))