# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário
# (se nota maior que 7 aprovado se não reprovado).
# No final, mostre o conteúdo gravado no dicionário. 

from typing import Generator
from typing import Dict

Dicio: Dict[str, str] = {}
def get_students() -> str:
    a: str = input('estudante:' )
    return a

def get_test() -> int:
    b: int = int(input('média: '))
    return b 

def média_check(media: int) -> str:
    if media < 7:
        c = "Reprovado"
    else:
        c = "Aprovado"
    return c



def main() -> None:
    nome = get_students()
    media = get_test()
    situacao = média_check(media)
    Dicio[nome] = situacao
    

while True:
    main()
    d = input("deseja adicionar mais alunos?: ").lower()
    if d == 'sim' or d == 's':
        continue
    else:
        print(Dicio)
        break

