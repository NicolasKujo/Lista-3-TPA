print("ola, eu sou um programa que ira calcular a media de notas da sua turma")
 
print()
 
turmas = int(input("insira o número de turmas:"))
 
print()
 
z = 0
 
while z < turmas:
 
 z = z + 1
 
 a = int(input("insira o numero de alunos na sala:"))
 
 b = 0
 
 d = 0
 
 maior = 0
 
 menor = 10
 
 while b < a:
 
  b = b + 1
  
  print() 
  
  c = int(input("insira a nota do aluno:"))
  
  print()
  
  d = d + c
  
  if c > maior:
  
    maior = 0
  
    maior = maior + c
  
  if menor > c:
  
    menor = 0
  
    menor = menor + c
 
 e = d / a
 
 print(e)
 
 print()
 
 print ("A maior nota foi " , maior)
 
 print()
 
 print ("A menor nota foi " , menor)
 
 print()
 
print("fim do programa")