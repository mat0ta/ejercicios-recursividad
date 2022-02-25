def Palindromo(palabra):
  palabra_upper = palabra.upper().split()
  if ''.join(palabra_upper) == ''.join(palabra_upper)[::-1]:
    print('Es palíndromo')
  else:
    print('No es palíndromo')