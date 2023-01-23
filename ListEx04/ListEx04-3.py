S = str(input())
A = str.lower(S)
D = ['a','e','i','o','u']
E = set(D)
F = ''.join(filter(lambda x: x not in E, S))
print(F)