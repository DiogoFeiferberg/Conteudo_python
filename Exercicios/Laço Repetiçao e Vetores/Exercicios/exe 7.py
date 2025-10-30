
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = (int(input("Digite o segundo número inteiro: ")))


if num1 > num2:
    num1, num2 = num2, num1

print(f"\nNúmeros inteiros no intervalo entre {num1} e {num2}:")


for numero in range(num1, num2 + 1):
    print(numero)

