
def teste_kargs(arg1, arg2, **kwargs):
    dict = {**kwargs}
    print(f'arg1 = {arg1}')
    print(f'arg2 = {arg2}')
    for i in dict.keys():
        print(f'{i} = {dict[i]}')

teste_kargs('Carro', 100, nome='jose', chave='teste',outrachave='brasil', oo='python')

#teste_kargs('Carro', 100, nome='jose', chave='teste')
