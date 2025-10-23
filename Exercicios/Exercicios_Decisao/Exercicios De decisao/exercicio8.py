preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))


if preco1 <= preco2 and preco1 <= preco3:
    print(f"O primeiro produto é o mais barato com o preço de R$ {preco1:.2f}")
elif preco2 <= preco1 and preco2 <= preco3:
    print(f"O segundo produto é o mais barato com o preço de R$ {preco2:.2f}")
else:
    print(f"O terceiro produto é o mais barato com o preço de R$ {preco3:.2f}")