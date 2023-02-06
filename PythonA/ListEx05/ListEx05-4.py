tl = 1
while tl %2 == 1:
    tl = int(input())
l = [int(input()) for _ in range(tl)]
la = []

for i in range(tl//2):
    la.append(l[i]+ l[tl-1])
    tl -= 1
print(la)