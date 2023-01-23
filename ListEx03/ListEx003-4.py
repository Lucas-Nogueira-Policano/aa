###**Exercício 003- 4:**Crie um programa que permita imprimir uma representação de um tabuleiro de xadrez.
###Entrada:
###O programa recebe um número inteiro, maior ou igual a 1, que indica a dimensão do tabuleiro. 



a = int(input())
c = a
b = a
while b > 0:
  while a != 0:
    print('o',end='')
    a = a - 1
    if a != 0:
      print('x',end='')
      a = a - 1
    else:
      print('')
      b = b - 1
  a = c
  if b == 0: 
    break