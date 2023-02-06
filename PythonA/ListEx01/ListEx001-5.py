###**Exercício 001-5:** Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 5% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais."""

nome = input('Insira o nome: ')
sF = float(input('Insira o Salario fixo: R$'))
tV = float(input('Insira a venda do mês: R$'))
C = (tV/100)*5
sT = C + sF
print('O total a receber por', nome, "é: R$", round(sT,2))