num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

numeros_ordenados = sorted([num1, num2, num3], reverse=True)
print(numeros_ordenados)