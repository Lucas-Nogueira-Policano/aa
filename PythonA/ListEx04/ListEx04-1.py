dP = 0
vR = 100
vK = 100

while True:
    golpe = int(input())
    if golpe == 0:
        break
    if golpe > 0:
        vK -= golpe
    if golpe < 0:
        vR += golpe
    if vK <= 0:
        dP += 1
        vR = 100
        vK = 100
    if vR <= 0:
        dP -= 1
        vR = 100
        vK = 100
    if dP == 5:
      break
    if dP == -5:
      break
if dP >= 5:
    print('Ryu Ganhou')
elif dP < 0:
    print('Ken Ganhou')    
else: 
    print('Empate')
        
