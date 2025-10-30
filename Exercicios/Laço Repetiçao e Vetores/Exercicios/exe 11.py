
soma_idades = 0
quantidade_pessoas = 0

print("Digite a idade das pessoas. Digite '0' para encerrar.")

while True:
    try:
        idade = int(input("Digite a idade de uma pessoa: "))


        if idade == 0:
            break

        if idade < 0:
            print("Por favor, insira uma idade válida.")
            continue

        soma_idades += idade
        quantidade_pessoas += 1

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        continue


if quantidade_pessoas > 0:
    media_idade = soma_idades / quantidade_pessoas


    if 0 <= media_idade <= 25:
        classificacao = "Jovem"
    elif 26 <= media_idade <= 60:
        classificacao = "Adulta"
    else:
        classificacao = "Idosa"

    print(f"\nA média de idade da turma é: {media_idade:.2f}")
    print(f"A turma é classificada como: {classificacao}")
else:
    print("\nNenhuma idade foi inserida para calcular a média.")

