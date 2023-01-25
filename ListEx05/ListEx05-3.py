la = input().split()
lb = input().split()
la = [int(A) for A in la]
lb = [int(A) for A in lb]
c = False
for a in la:
    for b in lb:
        if a == b:
            print (a)
            c = True
if not c:
    print('Nenhum elemento em comum')