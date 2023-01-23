###**Exercício 002- 4:** Faça um Programa que leia três números e mostre-os em ordem decrescente. 

a = int(input('digite o primeiro numero: '))
b = int(input('digite o segundo numero: '))
c = int(input('digite o terceiro numero: '))
d = (a, b, c)
if (b > a) and (a > c):
  d = (b, a, c)
if (b > a) and (c > a):
  d = (b, c, a)
if (c > a) and (b > a):
  d = (c, b, a)
if (c > a) and (a > b):
  d = (c ,a ,b)
print(d)