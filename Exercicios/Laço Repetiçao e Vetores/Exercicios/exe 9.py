
numero = int(input("Digite o número para ver a tabuada (de 1 a 100): "))


if 1 <= numero <= 100:
    print(f"Tabuada de {numero}:")

    for i in range(1, 1001):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
else:
    print("Por favor, insira um número entre 1 e 100.")


