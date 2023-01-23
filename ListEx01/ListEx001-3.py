###"""**Exercício 001-3:** A conversão de graus Fahrenheit para Celsius é dada pela expressão:

###**C . 1.8 = F - 32**
###e a conversão de Kelvin para graus Celsius é dada por
###**C = k - 273.15**

###Faça um programa que recebe como entrada a temperatura em graus Celsius e realize duas conversões: uma para Fahrenheit e outra para Kelvin.


C = float(input('Insira a temperatura em Celsius '))
F = C * 1.8 + 32
k = C + 273.15
print('Temperatura em Fahrenheit: ', round(F,1),'°F')
print('Temperatura em Kelvin ', round(k,1),"K")