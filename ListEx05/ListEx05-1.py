a = int(input())
v = []
for i in range(a):
    b = int(input())
    v.append(b)
for c in range(a):
    d = v[c]
    e = v[c+1]
    if e == d:
        print(f'pos {c} e {c+1}')
