print('Sabor Express')
print('\n')
print('1. Cadastrar Restaurante')
print('2. Listar Restaurantes')
print('3. Ativar Restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção:'))
print('Voce escolheu a opção', opcao_escolhida)
print(f'Voce escolheu a opção {opcao_escolhida}')
print(type(1))
print(type(opcao_escolhida))

if opcao_escolhida == 1:
    print('Cadastrar Restaurante')
elif opcao_escolhida == 2:
    print('Listar Restaurantes')
elif opcao_escolhida == 3:
    print('Ativar Restaurantes')
else:
    print('Encerrando Sistema')