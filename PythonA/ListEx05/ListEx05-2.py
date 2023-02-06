tl = int(input())
b = []
for i in range(tl):
    b.append(str(input()))
for j in range(tl):
    c = tl - j
    c -= 1
    print(b[c])
