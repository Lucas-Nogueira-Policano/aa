

#a = 0
a = "teste"
#a = 10 


try:
    result = 1/a
except TypeError:
    if type(a) == str:
        print(f"Impossivel dividir pois {a} não é um numero. {TypeError}")
        a = int(input('Por favor digite um numero: '))
        result = 1/a
        print(f'1/{a} = {result}')
except ZeroDivisionError:
    if a == 0:
        print(f"Opa, 0 não divide. {ZeroDivisionError}")
        q = input('gostaria de dar outro numero? ').lower
        if q == 'sim' or 'yes' or 's' or 'y':
            a = int(input('digite o novo divisor: '))
            result = 1/a
            print(f'1/{a} = {result}')
except Exception:
    print(f'Opa algum erro ocorreu: {type(Exception)}')
else:
    print(f'1/{a} = {result}')
finally:
    print(f"Por usar esse programa. Lucas Nogueira Policano agradece")