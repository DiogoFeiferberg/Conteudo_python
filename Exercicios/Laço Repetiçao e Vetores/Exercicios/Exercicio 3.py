populacao_a = 80000
taxa_a = 0.03 # 3%
populacao_b = 200000
taxa_b = 0.015 # 1.5%
anos = 0

while populacao_a < populacao_b:
    populacao_a = populacao_a + (populacao_a * taxa_a)
    populacao_b = populacao_b + (populacao_b * taxa_b)
    anos += 1

print(f"Serão necessários {anos} anos para a população do país A ultrapassar a do país B.")
