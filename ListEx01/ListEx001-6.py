###**Exercício 001-6:** Faça um programa que leia três números inteiros e apresente o maior dos três valores. ***Nesta questão está proibido usar if (isto é, não deve se usar nenhuma estrutura condicional)*** ou a função max, mas vai precisar usar a função abs(z) que retorna com o valor do módulo, sem sinal do parâmetro. **Dica**: A seguinte fórmula permite calcular o maior valor dados os números x e y:

###Max(x,y) = (x+y)/2 + abs(y-x)/2



a = int(input('Primeiro Numero: '))
b = int(input('Segundo Numero: '))
c = int(input('Terceiro Numero: '))
d = int((a+b)/2 + abs(b-a)/2)
e = int((d+c)/2 + abs(c-d)/2)
print('O Numero mais alto entre os inseridos foi:', e)