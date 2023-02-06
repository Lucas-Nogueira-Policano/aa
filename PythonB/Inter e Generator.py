## Crie uma função chamada “count_up” recebe x (int) e retorna um Generator
## que retorna os números menores que x da sequência:
## 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, … 
## onde a diferença de um termo da sequência para o anterior aumenta em uma unidade.

from typing import Generator

def count_up(limit: int) -> Generator[int, None, None]:
    a = 0
    c = 0
    b = iter(range(9999999))
    while c < limit:
        a = c + 1
        d = next(b)
        c = a + d
        yield a

for i in count_up(int(input())):
    print(i)