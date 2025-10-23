preco_gasolina = 6.29
preco_alcool = 4.17

tipo_combustivel = input("Informe o tipo de combustível (A para Álcool, G para Gasolina): ").upper()
litros = float(input("Informe o número de litros vendidos: "))

valor_a_pagar = 0

if tipo_combustivel == 'A':
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    preco_total = litros * preco_alcool
    valor_a_pagar = preco_total - (preco_total * desconto)
elif tipo_combustivel == 'G':
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    preco_total = litros * preco_gasolina
    valor_a_pagar = preco_total - (preco_total * desconto)
else:
    print("Tipo de combustível inválido.")

if valor_a_pagar > 0:
    print(f"O valor total a ser pago é: R$ **{valor_a_pagar:.2f}**")
