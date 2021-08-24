print ('ola, sou um programa que vai te ajudar com a tabuada, basta inserir um numero de 1 a 10 que eu mostrarei a tabuada dele')

print()

a = int(input('insira um numero de 1 a 10: '))

b = 8

d = 1

while a > 10 or a < 1:
  print()
  print ('so vale numeros de 1 a 10: ')
  print()
  a = int(input('insira um numero de 1 a 10: '))

c = a

print()

print (d, '  . ', a, ' = ' , a)

while b > 0:
  d = d + 1
  b = b - 1
  print (d, '  . ', a, ' = ' , c + a)
  c = c + a

print (10, ' . ', a, ' = ' , c + a)

print()

print('fim do programa')