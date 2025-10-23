import math

# Solicita o valor de 'a' ao usuário
try:
    a = float(input("Digite o valor de 'a': "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
    exit()

# a. Verifica se 'a' é igual a zero
if a == 0:
    print("O valor de 'a' não pode ser zero para uma equação do segundo grau. O programa será encerrado.")
else:
    # Solicita os valores de 'b' e 'c'
    try:
        b = float(input("Digite o valor de 'b': "))
        c = float(input("Digite o valor de 'c': "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        exit()

    # Calcula o delta (Δ)
    delta = b**2 - 4 * a * c
    print(f"O valor de delta é: {delta}")

    # b. Verifica se o delta é negativo
    if delta < 0:
        print("A equação não possui raízes reais.")
    # c. Verifica se o delta é igual a zero
    elif delta == 0:
        raiz = (-b) / (2 * a)
        print(f"A equação possui apenas uma raiz real: {raiz}")
    # d. Verifica se o delta é positivo
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"A equação possui duas raízes reais:")
        print(f"Raiz 1: {raiz1}")
        print(f"Raiz 2: {raiz2}")
