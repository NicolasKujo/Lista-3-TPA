print("Escreva dois numeros que eles irão ser dividos")

print()

a = int(input ("insira o primero número aqui:"))

print()

b = int(input ("insira o segundo número aqui:"))

print()

c = a / b

while b == 0 or a == 0:
  print ("não da para dividir zero, insira um valor valido")
  
  print()

  a = int(input ("insira o primero número aqui:"))
  
  print()
  
  b = int(input ("insira o segundo número aqui:"))

  print()

c = a / b

print (c)