# Inicializa variáveis
soma_idades = 0
quantidade_pessoas = 0

print("Digite a idade das pessoas. Digite '0' para encerrar.")

while True:
    try:
        idade = int(input("Digite a idade de uma pessoa: "))

        # Verifica se a idade é um valor válido para encerrar
        if idade == 0:
            break
        # Validação básica para garantir que a idade é positiva
        if idade < 0:
            print("Por favor, insira uma idade válida.")
            continue

        soma_idades += idade
        quantidade_pessoas += 1

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        continue

# Calcula a média apenas se houver pessoas
if quantidade_pessoas > 0:
    media_idade = soma_idades / quantidade_pessoas

    # Classifica a turma com base na média de idade
    if 0 <= media_idade <= 25:
        classificacao = "Jovem"
    elif 26 <= media_idade <= 60:
        classificacao = "Adulta"
    else:  # media_idade > 60
        classificacao = "Idosa"

    print(f"\nA média de idade da turma é: {media_idade:.2f}")
    print(f"A turma é classificada como: {classificacao}")
else:
    print("\nNenhuma idade foi inserida para calcular a média.")

