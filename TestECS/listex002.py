# -*- coding: utf-8 -*-
###ListEx002

###Automatically generated by Colaboratory.

###Original file is located at
###    https://colab.research.google.com/drive/1o5acmUd1goCf1Nfu98ttkuA7PbW2MPAs

###Exercício 002-1:** Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


valor = int(input('Digite o numero: '))
if (valor >= 0):
  print('Seu numero', valor, 'é positivo')
else:
  print('Seu numero', valor, 'é negativo')

###**Exercício 002-2:** Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 



sexualidade = str(input('Insira seu sexo(Por favor ultilize apenas F ou M): '))
if (sexualidade == 'M'):
  print('Individuo do Sexo Masculino')
elif(sexualidade == 'F'):
  print('Individuo do Sexo Feminino')
else:
  print('Sexo Inválido, por favor ultilize apenas F ou M')

###**Exercício 002-3:** Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 



letra = str(input('Insira a letra: '))
if letra == ("a") and ("e") and ("i") and ("o") and ("u"):
  print('Sua letra é uma vogal')
else:
  print('Sua letra é uma consoante')

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

###**Exercício 002-5:** As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores. Eles contrataram você para desenvolver o programa que calculará os reajustes. 

###Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual: 

###salários até RS 280,00 (incluindo) : aumento de 20% 

###salários entre RS 280,00 e RS 700,00 : aumento de 15% 

###salários entre RS 700,00 e RS 1500,00 : aumento de 10% 

###salários de RS 1500,00 em diante : aumento de 5% 

###Após o aumento ser realizado, informe na tela: 

###o salário antes do reajuste; 

###o percentual de aumento aplicado; 

###o valor do aumento; 

###o novo salário, após o aumento. 



St = float(input('Salario atual: R$'))
if (St <= 280):
  Sa = (St*20/100)
  Pa = 20
elif(St < 700):
  Sa = (St*15/100)
  Pa = 15
elif(St <= 1500):
  Sa = (St*10/100)
  Pa = 10
elif(St > 1500):
  Sa = (St*5/100)
  Pa = 5
Ns = round((St + Sa),2)
Sa = round(Sa,2)
St = round(St,2)
print('Salario anterior: R$',St)
print('Aumento aplicado(em %): ',Pa,'%')
print('Aumento aplicado(em R$): ',Sa)
print('Novo Salario: R$',Ns)

###**Exercício 002-6:** Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. 

###Desconto do IR: 

###Salário Bruto até 900 (inclusive) - isento 

###Salário Bruto até 1500 (inclusive) - desconto de 5% 

###Salário Bruto até 2500 (inclusive) - desconto de 10% 

###Salário Bruto acima de 2500 - desconto de 20%   

###Imprima na tela as informações, 
###dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.


###Salário Bruto: (5 * 220)  : RS 1100,00 (-) 

###IR (5%)  : RS 55,00 (-) 

###INSS ( 10%)  : RS 110,00 

###FGTS (11%)  : RS 121,00 

###Total de descontos  : RS 165,00

###Salário Liquido  : RS 935,00



Va = float(input('Informe o valor da sua hora: R$'))
qtdT = float(input('Informe suas horas trabalhas: '))
qtdT = round(qtdT,2)
Sb = Va * qtdT
Fgts = (Sb)*11/100
Inss = (Sb)*10/100
Sind = (Sb)*3/100
if ((Sb) <= 900 ):
  Sl = float(Sb - Sind - Inss)
elif ((Sb) <= 1500 ):
  Sl = float((Sb) - (Sb)*5/100 - Sind - Inss)
  Ir = (Sb)*5/100
  Dir = 5
elif ((Sb) <= 2500 ):
  Sl = float((Sb) - (Sb)*10/100 - Sind - Inss)
  Ir = (Sb)*10/100
  Dir = 10
else:
  Sl = float((Sb) - (Sb)*20/100 - Sind - Inss)
  Ir = (Sb)*20/100
  Dir = 20
Td = Sb - Sl
print('Salario bruto: (',Va,'*',qtdT,'): R$',Sb)
print('IR(',Dir,'%) R$',Ir)
print('INSS(10%): R$',Inss)
print('FGTS(11%): R$',Fgts)
print('Sindicato(3%): R$',Sind)
print('Total de descontos: R$', round(Td,2))
print('Salário Liquido: R$', round(Sl,2))

###Versão com IR atualizado
Va = float(input('Informe o valor da sua hora: R$'))
qtdT = float(input('Informe suas horas trabalhas: '))
qtdT = round(qtdT,2)
Sb = Va * qtdT
Fgts = (Sb)*11/100
Inss = (Sb)*10/100
Sind = (Sb)*3/100
Impr = 0
if ((Sb) <= 900 ):
  Sl = float(Sb - Sind - Inss)
elif ((Sb) <= 1500 ):
  Sb = Sb - 900
  Ir = (Sb)*0.05
  Sl = float((Sb) - Ir - Sind - Inss)
  Dir = 52
elif ((Sb) <= 2500 ):
  Sb = Sb - 900
  Ir = (Sb)*0.1
  Sl = float((Sb) - Ir - Sind - Inss)
  Dir = 10
else:
  Sb = Sb - 900
  Ir = (Sb)*0.2
  Sl = float((Sb) - Ir - Sind - Inss)
  Dir = 20
Td = Sb - Sl
print('Salario bruto: (',Va,'*',qtdT,'): R$',Sb)
print('IR(',Dir,'%) R$',Ir)
print('INSS(10%): R$',Inss)
print('FGTS(11%): R$',Fgts)
print('Sindicato(3%): R$',Sind)
print('Total de descontos: R$', round(Td,2))
print('Salário Liquido: R$', round(Sl,2))

###**Exercício 002-7:** O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira: 

###Até 5 Kg Acima de 5 Kg File Duplo RS 4,90 por Kg RS 5,80 por Kg Alcatra RS 5,90 por Kg RS 6,80 por Kg Picanha RS 6,90 por Kg RS 7,80 por Kg Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 



qtdC = float(input('Informe a quantidade de carne(Kg): '))
tpC = str(input('Informe o tipo de carne: '))
tP = 0
if (tpC == 'File Duplo') and (qtdC <= 5):
  tP = qtdC*4.9
elif (tpC == 'File Duplo') and (qtdC > 5):
  tP = qtdC*5.8
elif(tpC == 'Alcatra') and (qtdC <= 5):
  tP = qtdC*5.9
elif(tpC == 'Alcatra') and (qtdC > 5):
  tP = qtdC*6.8
elif(tpC == 'Picanha') and (qtdC <= 5):
  tP = qtdC*6.9
elif(tpC == 'Picanha') and (qtdC > 5):
  tP = qtdC*7.8
else:
  print('Produto fora da promoção') 
Tp = str(input('Informe o tipo de pagamento: '))
if (Tp == 'Cartão Tabajara'):
  tp = tP - (tP*5/100)
else:
  tp = tP
d = tP - tp
print('\t\tCupom fiscal')
print('Produto:',tpC,'------ Quantidade:',qtdC,'Kg')
print('Preço Total: R$',tP)
print('Tipo de pagamento:',Tp)
print('Desconto aplicado: R$',round(d,2))
print('Total a Pagar: R$',round(tp,2))