usuario_determinado = "usuario"
senha_determinada = "senha"
print("Acesso ao Sistema")
usuario_inserido = input("Usuario: ")
senha_inserida = input("Senha: ")
if usuario_determinado == usuario_inserido and senha_determinada == senha_inserida:
    print(f"Acesso Permitido. Seja bem-vindo, {usuario_determinado}!")
else:
    print("Acesso Negado. Tente novamente.")