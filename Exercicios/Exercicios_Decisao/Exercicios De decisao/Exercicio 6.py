num1 = float(input("digite o numero1:"))
num2 = float(input("Digite o numero2:"))
num3 = float(input("Digite o numero3:"))
if num1 >= num2 and num1 >= num3:
    maior_numero = num1
elif num2 >= num1 and num2 >= num3:
    maior_numero = num2
else:
    maior_numero = num3
print(f"O maior número é: {maior_numero}")
