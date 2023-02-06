a = str(input())
b = str(input())
c = ''.join(d + e for d,e in zip(a,b))
print(str(c))