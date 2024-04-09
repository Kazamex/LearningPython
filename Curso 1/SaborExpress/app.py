import os
def exibir_menu():
    print('Sabor Express')
    print('\n')
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def escolher_opcao():
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
        encerrar_app()

def encerrar_app():
    os.system('cls')
    print('Finalizando App.\n')

def main():
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()