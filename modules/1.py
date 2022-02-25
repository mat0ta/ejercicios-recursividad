palabras = ['Rusia', 'Paco', 'Platano', 'Ordenador']
posicion = -1

def Busqueda(palabra):
  global posicion
  posicion += 1
  if posicion < len(palabras):
    if str(palabras[posicion]).lower() == str(palabra).lower():
      return print('La palabra ' + str(palabra).upper() + ' está en la posicion ' + str(posicion + 1))
    Busqueda(palabra)
  elif posicion == len(palabra):
    print('La palabra no está en la lista.')

Busqueda('RUSIA')