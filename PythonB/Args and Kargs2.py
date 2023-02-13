def multiplicador_args(*args: list[int]) -> int:
    a = 1
    d = 0
    for x in args:
        for i in x:
            a *= i
    return print(a)
c =[]
while True:
    b = int(input())
    if b != 0 and b != '':
        c.append(b)
    else: 
        multiplicador_args(c)
        break


