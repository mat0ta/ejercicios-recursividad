# Ejercicio 3 - La bandera de Dijkstra
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