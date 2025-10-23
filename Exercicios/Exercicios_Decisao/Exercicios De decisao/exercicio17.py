def caixa_eletronico():
    # Notas disponíveis em ordem decrescente
    notas = [100, 50, 10, 5, 1]

    while True:
        try:
            # Solicita o valor do saque ao usuário
            valor_saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))

            # Verifica se o valor está dentro do intervalo permitido
            if 10 <= valor_saque <= 600:
                break  # Sai do loop se o valor for válido
            else:
                print("Valor inválido. Por favor, digite um valor entre 10 e 600.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    print(f"\nSaque de R$ {valor_saque}:")

    # Percorre a lista de notas para determinar a quantidade de cada uma
    for nota in notas:
        if valor_saque >= nota:
            quantidade = valor_saque // nota
            print(f"{quantidade} nota(s) de R$ {nota}")
            valor_saque %= nota  # Atualiza o valor restante após distribuir as notas


# Chama a função principal para iniciar o programa
caixa_eletronico()