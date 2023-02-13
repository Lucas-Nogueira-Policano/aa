from typing import List
def teste_args(a, b, *args) -> None:
    list_args = [*args]
    c = iter(range(99999999))
    print(f'arg{next(c)+1}:{a}')
    print(f'arg{next(c)+1}:{b}')
    for x in list_args:
        print(f'arg{next(c)+1}:{x}')

teste_args('brasil', 'País', 'Mundo', 'Carro', 100, 50, 'Pedra')

#teste_args('brasil', 'País', 'Gol', 'Carro', 10)