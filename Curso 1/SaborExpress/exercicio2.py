numero_inserido = int(input('Por gentileza insira um número: '))
sobra = numero_inserido % 2
if sobra == 1:
    print(f'O número {numero_inserido} é ímpar')
else:
    print(f'O número {numero_inserido} é par')