###**Exercício 003-5:** Ao observar a curva de velocidade de um motor, um engenheiro percebeu que sempre ocorria
###uma queda de velocidade quando medições eram feitas em intervalos de 10 ms. Após realizar alguns testes, ele
###observou que tais quedas não ocorriam necessariamente no mesmo momento. Intrigado pela falta de padrão,
###agora ele quer a sua ajuda para saber: dado um caso de teste, qual a primeira medição em que ocorreu uma
###queda de velocidade? 


N = int(input('Velocidade do motor: '))
ant = int(0)
b = 0
c = 0

for i in range(N):
  a = int(input('RPM: '))
  if (c == 0 and a < ant):
    b = (i + 1)
    c = 1
  elif (c == 0 and i + 1 == N):
    b = 0
  else:
    ant = a

print(b)