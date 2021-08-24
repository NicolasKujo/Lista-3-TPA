print("insira suas notas e eu mostrarei a sua media, não vale numeros maiores que 10 ou menores que 0")

e = 1

while e < 3: 

  print()

  a = int(input("insira sua primeira nota:"))

  print()

  b = int(input("insira sua segunda nota:"))
  
  c = a + b 

  d = c / 2

  e = e + 1

  while a > 10 or a < 0:
    
    print()

    print ("não vale numeros maiores que 10 ou menores que 0")

    print()

    a = int(input("insira sua primeira nota:"))

    print()

    b = int(input("insira sua segunda nota:"))

    c = a + b 

    d = c / 2

  print()
  print(d)

print()
print ("fim do programa")