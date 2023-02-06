###**Exercício 002-2:** Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 



sexualidade = str(input('Insira seu sexo(Por favor ultilize apenas F ou M): '))
if (sexualidade == 'M'):
  print('Individuo do Sexo Masculino')
elif(sexualidade == 'F'):
  print('Individuo do Sexo Feminino')
else:
  print('Sexo Inválido, por favor ultilize apenas F ou M')