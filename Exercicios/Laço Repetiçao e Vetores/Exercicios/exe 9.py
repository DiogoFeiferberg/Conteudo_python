
numero = int(input("Digite o número para ver a tabuada (de 1 a 10): "))


if 1 <= numero <= 10:
    print(f"Tabuada de {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
else:
    print("Por favor, insira um número entre 1 e 10.")


