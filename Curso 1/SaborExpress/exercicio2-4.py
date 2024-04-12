import os
os.system('cls')
print("Bem-vindo! Ao sistema de identificação de quandrante!")
x = int(input("Informe o valor de X: "))
y = int(input("Informe o valor de Y: "))
if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante!")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante!")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante!")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante!")
else:
    print("O ponto está no ponto de origem ou em um dos eixos!")