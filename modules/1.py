# Ejercicio 1 - Búsqueda por dicotomía en una tabla ordenada
palabras = ['Rusia', 'Rococo', 'Ramadan', 'Roedor', 'Alimento']
palabras.sort()
posicion = len(palabras) // 2
repeticiones = 1
index = 0
print(palabras)

def Busqueda(palabra):
  global posicion, index, repeticiones
  palabra = palabra.upper()
  if palabras[posicion].upper() == palabra:
    return print('Has encontrado la palabra ' + palabra + ' en la posición ' + str(posicion + 1) + ' (Index '+ str(posicion) + ')')
  else:
    if palabra[0] > palabras[posicion].upper()[0] and palabra[0] != palabras[posicion].upper()[0]:
      print('Palabra esta a la derecha')
      posicion += 1
      Busqueda(palabra)
    elif palabra[0] < palabras[posicion].upper()[0] and palabra[0] != palabras[posicion].upper()[0]:
      print('Palabra esta a la izquierda')
      posicion -= 1
      Busqueda(palabra)
    elif palabra[0] == palabras[posicion].upper()[0]:
      print('Palabra esta a la izquierda o a la derecha')
      if palabra[index] == palabras[posicion + 1].upper()[index] and palabra[index] != palabras[posicion - 1].upper()[index]:
        print('Palabra esta a la derecha')
        posicion += 1
        Busqueda(palabra)
      elif palabra[index] == palabras[posicion - 1].upper()[index] and palabra[index] != palabras[posicion + 1].upper()[index]:
        print('Palabra esta a la izquierda')
        posicion -= 1
        Busqueda(palabra)
      elif palabra[index] == palabras[posicion - 1].upper()[index] and palabra[index] == palabras[posicion + 1].upper()[index]:
        print('Palabra esta a la izquierda o a la derecha - 2')
        if index % 2 == 0:
          index += (1 * repeticiones)
          repeticiones += 1
        else:
          index -= (1 * repeticiones)
          repeticiones += 1
        Busqueda(palabra)

Busqueda('roedor')