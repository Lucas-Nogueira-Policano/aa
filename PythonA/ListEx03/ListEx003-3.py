###**Exercício 003-3:**Crie um programa que permita verificar se um número N é fatorial ou não. N é fatorial caso
###exista um número X >= 0 tal que N = X!. 



n = int(input())
e = int(1)
b = int(1)
while n != e:
  if n != e:
      e = e*b
      b = b + 1
  if e > n:
    break
if n == e:
  print('Verdadeiro')   
else:
    print('Falso')