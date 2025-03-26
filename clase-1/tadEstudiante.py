def crearEstudiante():
    return {
        "nombre": "",
        "notas": [],
        "legajo": ""
    }

def cargarEstudiante(estudiante, nombre, legajo):
    estudiante["nombre"] = nombre
    estudiante["legajo"] = legajo

def agregarNota(estudiante, nota):
    estudiante["notas"].append(nota)

def cambiarNombre(estudiante, nuevoNombre):
    estudiante["nombre"] = nuevoNombre

def cambiarLegajo(estudiante, nuevoLegajo):
    estudiante["legajo"] = nuevoLegajo

def promedio(estudiante):
  if len(estudiante["notas"]) == 0:
    return 0
  else:
    return sum(estudiante["notas"]) / len(estudiante["notas"])