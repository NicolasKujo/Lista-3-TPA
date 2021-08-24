from random import randint

print ('você tem 3 tentativas para acertar um numero gerado aleatoriamente entre 0 a 10, em cada tentaiva você não deve colocar o mesmo numero, pois o numero sorteado não muda ate o fim da partida, mas então bora lá')

print()

a = int(input('insira o valor de 0 a 10:'))

c = 2

b = 1

if (a > 10):
  print()
  print ('so vale numeros entre 0 a 10')

if randint(0, 10) == a:
  print ("Um verdadeiro Guru")
  exit(0) 

while (b < c):
  print()
  da = int(input('errou, insira novamente:'))
  print()
  d = int(input('você realmente não tem sorte, insira novamente:'))
  b = b + 1
  if (d > 10):
    print()
    print ('eu ja tinha avisado que era numero de 0 a 10, perdeu o jogo')
    exit(0)  
  if (d == randint(0, 10)):
    print()
    print ('Um verdadeiro Guru')
    exit(0)
  if (da == randint(0, 10)):
    print()
    print ('Um verdadeiro Guru')
    exit(0)

if (d != a):
  print()
  print ('acabaram suas tentativas') 