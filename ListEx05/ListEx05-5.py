a = int(input())
V =[]
d =[]
if a%2 != 0:
    for i in range(a):
        V.append(int(input()))
    for j in range(a):
        c = a - j
        c -= 1
        d.append(V[c])
    for k in range(len(V)//2):
        if V[k] >= d[k]:
            V[k] = d[k]
            e = a - 1
            V[e-k] = d[e-k]
        else:
            continue
print (V)