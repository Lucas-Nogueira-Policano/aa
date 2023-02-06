### Defina uma função chamada weird_prod que recebe como argumento uma lista de números inteiros
### e devolve o produto do primeiro elemento, pelo quadrado do segundo, pelo cubo do terceiro,
### e assim sucessivamente.


from typing import List
from functools import  reduce
elv: List[int] = []
c = 1
def weird_prod(a: int, b: int) -> int:
    """Recebe os inteiros e devolve o produto do quadrado do primeiro, pelo quadrado do segundo, pelo cubo do terceiro, etc..."""
    global c 
    c += 1
    return a*(b**c)
list_int = input().split()
count = list(map(int, list_int))
bababuia = reduce(weird_prod, count)
print(bababuia)