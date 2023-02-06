from typing import List

def get_user_words() -> List[str]:
    """Recebe a lista -- Não é uma função pura"""
    a: List[str] = input().split()
    return a

def count_x(word: str) -> int:
    """"Conta a ocorrencia de X por palavra -- É pura"""
    return word.count('x')

def info_avg(total: float) -> None:
    """Informa a ocorrencia de X na lista -- É pura"""
    print(f'ocorrencias de x: {total:.0f}%')

def main() -> None:
    """"Cabeça do programa -- Não é pura"""
    words: List[str] = get_user_words()
    To:int = 0
    Tl:int = 0
    for word in words:
        To += count_x(word)
        Tl += len(word)
    total:float = (To/Tl)*100
    info_avg(total)

if __name__ == '__main__':
    main()