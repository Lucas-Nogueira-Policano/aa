###**Exercício 001-7:** Faça um programa que leia um valor inteiro representando um valor em reais e calcule o menor número de cédulas possíveis no qual o valor pode ser decomposto. As cédulas consideradas são as de RS200.00, RS100.00, RS50.00, RS20.00, RS10.00, RS5.00, RS2.00 e RS1.00. Seu programa deve imprimir a quantidade de cada cédula. Dica: divisão inteira usa // e resto da divisão usa %

###Assim valor total RS 1317,00 quantas notas de RS 200,00

###qtdNotas200 = valorTotal // 200

###resulta 6 notas de 200 e agora o resto seria

###restoValor = valorTotal % 200

###resulta 117


Vt = float(input('Insira o valor: R$'))
qtdA = int(Vt // 200)
qtdB = int(Vt % 200)
qtdC = int(qtdB // 100)
qtdD = int(qtdB % 100)
qtdE = int(qtdD // 50)
qtdF = int(qtdD % 50)
qtdG= int(qtdF // 20)
qtdH= int(qtdF % 20)
qtdI= int(qtdH // 10)
qtdJ= int(qtdH % 10)
qtdK= int(qtdJ // 5)
qtdL= int(qtdJ % 5)
qtdM= int(qtdL // 2)
qtdN= int(qtdL % 2)
qtdO= int(qtdN // 1)
print('No total serão usadas', qtdA, ' notas de R$200. ', qtdC, 'notas de R$100. ', qtdE, 'notas de R$50. ', qtdG, 'notas de R$20. ', qtdI, 'notas de R$10. ', qtdK, 'notas de R$5. ', qtdM, 'notas de R$2 e ', qtdO, 'moedas de R$1.'  )