valor_hora = float(input("Digite o valor da sua hora: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))


salario_bruto = valor_hora * horas_trabalhadas


if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
else:
    desconto_ir = salario_bruto * 0.20


desconto_sindicato = salario_bruto * 0.03


total_descontos = desconto_ir + desconto_sindicato


salario_liquido = salario_bruto - total_descontos


print(f"\n--- Folha de Pagamento ---")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"(-) IR: R$ {desconto_ir:.2f}")
print(f"(-) Sindicato (3%): R$ {desconto_sindicato:.2f}")
print(f"Total de Descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
print("--------------------------")