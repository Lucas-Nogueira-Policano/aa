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