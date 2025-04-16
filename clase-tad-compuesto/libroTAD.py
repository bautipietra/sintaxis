def crearLibro():
  return {}

def cargarLibro(libro, titulo, autor, editorial, precio):
  libro["titulo"] = titulo
  libro["autor"] = autor
  libro["editorial"] = editorial
  libro["precio"] = precio

def modificarTitulo(libro, titulo):
  libro["titulo"] = titulo

def modificarAutor(libro, autor):
  libro["autor"] = autor 

def modificarEditorial(libro, editorial):
  libro["editorial"] = editorial 

def modificarPrecio(libro, precio):
  libro["precio"] = precio 

def obtenerTitulo(libro):
  return libro["titulo"]

def obtenerAutor(libro):
  return libro["autor"]

def obtenerEditorial(libro):
  return libro["editorial"]

def obtenerPrecio(libro):
  return libro["precio"]

