import string
import re
con = 0
vog = 0
sin = 0
F = str.lower(input())
v = ['a','e','i','o','u']
a = list(string.ascii_lowercase)
p = str(string.punctuation)
for letra in F:
  for vv in v:
     if letra == vv:
            vog += 1  
  for va in a:
    if letra == va:
            con += 1
  for vp in p:
    if letra == vp:
            sin += 1
con = (con - vog)       
n = int(len(F))
esp = n - (con + vog + sin)
qT = n
pV = round(float(vog/qT*100),2)
pC = round(float(con/qT*100),2)
pE = round(float(esp/qT*100),2)
pP = round(float(sin/qT*100),2)
print('quantidade total: ', n)
print(f'Consoantes: {pC}%')
print(f'Vogais: {pV}%')
print(f'Pontuações: {pP}%')
print(f'Espaços: {pE}%')