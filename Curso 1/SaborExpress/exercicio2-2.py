print("Bem-vindo ao sistema de indentificação de faixa etária!")
idade = int(input("Por favor insira a sua idade: "))
if idade > 0 and idade <= 12 :
    print(f"Você tem {idade} anos. Você é uma criança!")
elif idade > 12 and idade < 18:
    print(f"Você tem {idade} anos. Voce é um(a) adoslecente!")
elif idade >= 18 and idade < 200:
    print(f"Você tem {idade} anos. Você é um adulto!")
else:
    print("Idade inválida. Por gentileza insira uma idade válida.")