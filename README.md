<h1 align="center">Ejercicios de Recursividad</h1>
<p> Para realizar esta actividad he utilizado la herramienta <a href="https://replit.com/">Replit</a></p>

***

<h2>Ejercicio 1. Búsqueda por dicotomía en una tabla ordenada</h2>

Dada una tabla desordenada alfabéticamente se pide crear un algoritmo que la ordene y busque la posición en la misma de una palabra en específico. 
La función empleada para crear dicho algoritmo es la siguiente:

```py
palabras = ['Rusia', 'Rococo', 'Ramadan', 'Roedor', 'Alimento']
palabra = " "
posicion = len(palabras) // 2
repeticiones = 1
index = 0

def Busqueda():
  global posicion, index, repeticiones, palabra
  print(palabras)
  if palabra == " ":
    palabra = str(input("Introduce una palabra que buscar entre las palabra de la lista:"))
  palabras.sort()
  palabra = palabra.upper()
  if palabras[posicion].upper() == palabra:
    return print('Has encontrado la palabra ' + palabra + ' en la posición ' + str(posicion + 1) + ' (Index '+ str(posicion) + ')')
  else:
    if palabra[0] > palabras[posicion].upper()[0] and palabra[0] != palabras[posicion].upper()[0]:
      print('Palabra esta a la derecha')
      posicion += 1
      Busqueda()
    elif palabra[0] < palabras[posicion].upper()[0] and palabra[0] != palabras[posicion].upper()[0]:
      print('Palabra esta a la izquierda')
      posicion -= 1
      Busqueda()
    elif palabra[0] == palabras[posicion].upper()[0]:
      print('Palabra esta a la izquierda o a la derecha')
      if palabra[index] == palabras[posicion + 1].upper()[index] and palabra[index] != palabras[posicion - 1].upper()[index]:
        print('Palabra esta a la derecha')
        posicion += 1
        Busqueda()
      elif palabra[index] == palabras[posicion - 1].upper()[index] and palabra[index] != palabras[posicion + 1].upper()[index]:
        print('Palabra esta a la izquierda')
        posicion -= 1
        Busqueda()
      elif palabra[index] == palabras[posicion - 1].upper()[index] and palabra[index] == palabras[posicion + 1].upper()[index]:
        print('Palabra esta a la izquierda o a la derecha - 2')
        if index % 2 == 0:
          index += (1 * repeticiones)
          repeticiones += 1
        else:
          index -= (1 * repeticiones)
          repeticiones += 1
        Busqueda()
```

<h2>Ejercicio 2. Palíndromos</h2>

El ejercicio requiere de la creación de un algoritmo que indique si una palabra introducida es palíndromo o no.
La función empleada para crear dicho algoritmo es la siguiente:

```py
import unidecode

def Palindromo(palabra):
  palabra = unidecode.unidecode(palabra.replace(" ", ""))
  palabra_upper = palabra.upper().split()
  if ''.join(palabra_upper) == ''.join(palabra_upper)[::-1]:
    print('Es palíndromo')
  else:
    print('No es palíndromo')
```

<h2>Ejercicio 3. La bandera de Dijkstra</h2>

Dada una lista de colores desordenada pide que esta sea ordenada por colores empleando recursividad.
La función empleada para crear dicho algoritmo es la siguiente:

```py
r = 'ROJO'
a = 'AZUL'
v = 'VERDE'

bandera = [r, a, a, r, v, a, a, r, a, r, r, v, r, r, a, v, v]
bandera_ordenada = []
posicion = -1
posicion_ = -1
azul, rojo, verde = 0, 0, 0

def Bandera():
  global bandera, r, a, v, posicion, posicion_, bandera_ordenada
  global azul, rojo, verde
  posicion += 1
  if posicion < len(bandera):
    if str(bandera[posicion]) == r:
      rojo = rojo + 1
      return Bandera()
    elif str(bandera[posicion]) == v:
      verde = verde + 1
      return Bandera()
    elif str(bandera[posicion]) == a:
      azul = azul + 1
      return Bandera()
    Bandera()
  posicion_ += 1
  if posicion_ < len(bandera):
    if str(bandera[posicion_]) == r and len(bandera_ordenada) < rojo:
      bandera_ordenada.append(r)
      Bandera()
      return
    elif str(bandera[posicion_]) == v and len(bandera_ordenada) >= rojo and len(bandera_ordenada) < (rojo + verde):
      bandera_ordenada.append(v)
      Bandera()
      return
    elif str(bandera[posicion_]) == a and len(bandera_ordenada) >= (rojo + verde)  and len(bandera_ordenada) < (rojo + verde + azul):
      bandera_ordenada.append(a)
      Bandera()
      return
    Bandera()
    if posicion_ >= len(bandera) and len(bandera_ordenada) < len(bandera):
      posicion_ = 0
      Bandera()
  elif len(bandera) == len(bandera_ordenada):
    print(bandera_ordenada)
```
