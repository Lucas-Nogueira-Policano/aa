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