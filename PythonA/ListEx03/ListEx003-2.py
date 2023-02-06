###**Exercício 003-2:** Faça um temporizador de segundos (contagem regressiva) que passe a atualizar o tempo mais
##raramente. A contagem com o intervalo entre cada atualização fique dois segundos maior após cada uma delas.
##Por exemplo, se ele iniciar o temporizador com 50 segundos, então receberá atualizações dizendo que faltam 50,
##48, 44, 38, 30, 20 e 8 segundos (note que os intervalos entre as notificações foram 2, 4, 6, 8, 10 e 12 segundos).
##Desenvolva um programa que exiba em quais segundos o temporizador receberá atualizações, dado que o
##programa tenha sido inicializado com um tempo igual a N. 
import time


Ti = int(input('Tempo inicial: '))
Rg =0
while Ti > 0:
  if Ti:
    Ti = int(Ti - Rg)
    time.sleep(Rg)
    if Ti > 0:
      print('Faltam ',Ti,' segundos')
    else:
      print('Acabou')
  Rg = Rg + 2