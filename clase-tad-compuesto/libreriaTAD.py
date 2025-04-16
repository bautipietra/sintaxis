# Crear librería

def crearLibreria():
  return []

def agregarLibro(libreria, libro):
  libreria.append(libro)

def eliminarLibro(libreria, libro):
  libreria.remove(libro)

def obtenerLibro(libreria, i):
  if (i >= tamanioLibreria(libreria)):
    return "No se encontró un libro en esa posición"
  else:
    return libreria[i]

def obtenerTodosLosLibros(libreria):
  return libreria

def tamanioLibreria(libreria):
  return len(libreria)

def existeLibro(libreria, libro):
  return libro in libreria

def obtenerLibrosPorEditorial(libreria, editorial):
    def filtroPorEditorial(libro):
        return libro["editorial"] == editorial
    return list(filter(filtroPorEditorial, libreria))