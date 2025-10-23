def calcular_reajuste_salarial():
    salario_atual = float(input("Digite o salário atual do colaborador: R$ "))


    percentual_aumento = 0
    valor_aumento = 0
    novo_salario = 0


    if 0 <= salario_atual <= 1450.00:
        percentual_aumento = 0.20  # 20%
    elif 1450.00 < salario_atual <= 2800.00:
        percentual_aumento = 0.15  # 15%
    elif 2800.00 < salario_atual <= 3500.00:
        percentual_aumento = 0.10  # 10%
    else:
        percentual_aumento = 0.05  # 5%


    valor_aumento = salario_atual * percentual_aumento
    novo_salario = salario_atual + valor_aumento


    print(f"\n--- Reajuste Salarial ---")
    print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
    print(f"Percentual de aumento: {percentual_aumento * 100:.0f}%")
    print(f"Valor do aumento: R$ {valor_aumento:.2f}")
    print(f"Novo salário: R$ {novo_salario:.2f}")


calcular_reajuste_salarial()