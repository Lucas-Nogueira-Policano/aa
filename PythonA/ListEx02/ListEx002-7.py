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