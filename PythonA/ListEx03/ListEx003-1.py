###**Exercício 003-1:** Desenvolva um programa que simule o funcionamento de uma máquina de somar.
###Entrada:
###O seu programa receberá um número inteiro não negativo N que denota a quantidade de números que seu
###programa receberá para computar o valor total da soma. Na sequência seu programa receberá N números reais.
###Saída:


n = int(input('Insira a quantidade de variaveis: '))
Na = float(0)
while n > 0:
  Na = Na + float(input())
  n = n-1
print('Total: ',round(Na,2))