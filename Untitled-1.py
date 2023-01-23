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
