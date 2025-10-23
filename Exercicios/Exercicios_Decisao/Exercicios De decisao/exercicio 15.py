# Solicita os valores dos três lados ao usuário
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

# 1. Verifica se os valores podem formar um triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    # 2. Se for um triângulo, classifica-o
    if a == b and b == c:
        print("Os lados formam um triângulo Equilátero.")
    elif a == b or a == c or b == c:
        print("Os lados formam um triângulo Isósceles.")
    else:
        print("Os lados formam um triângulo Escaleno.")
else:
    print("Os valores informados não formam um triângulo.")