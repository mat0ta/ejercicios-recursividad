import sys
sys.path.insert(1, './modules')
from modules import e1, e2, e3

array_ejercicios = {
  1: 'e1.Busqueda()',
  2: 'e2.Palindromo(str(input("Introduce una palabra/s para comprobar si se trata o no de un palíndromo: ")))',
  3: 'e3.Bandera()',
}

if __name__ == "__main__":
  start = input('Bienvenido a la plataforma de ejercicios de recursividad. Por favor, introduzca el número del ejercicio que quiere probar (1 a 3) o introduzca 0 para salir: ')
  while int(start) >= 1 and int(start) <= 3:
    eval(str(array_ejercicios[int(start)]))
    start = input('Por favor, introduzca el número del ejercicio que quiere probar (1 a 3) o introduzca 0 para salir: ')