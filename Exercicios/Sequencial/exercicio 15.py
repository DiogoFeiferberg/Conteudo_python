import math
pergunta = float(input("Quanto voce ganha por hora?:  "))
pergunta2 = float(input("e quantas horas voce trabalhou?:  "))
salario = (pergunta * pergunta2)
INSS = 0.08
Imposto_de_renda = 0.11
Sindicato = 0.05
Desconto_INSS = 0.08 * salario
Desconto_sindicato = 0.05 * salario
Desconto = INSS + Imposto_de_renda + Sindicato
salario2 = salario * Desconto

print("com isso o meu desconto do salario foi de",Desconto)
print("meu salario foi de",salario2)
#PARTE 2
print("o salario bruto foi de",salario)
#PARTE 3
print("o tanto que o Inss recebeu foi de",Desconto_INSS)
#PARTE 4
print("o tanto que o Sindicato recebeu foi de",Desconto_sindicato)
#PARTE 1
print("o salario liquido foi de",salario2)

