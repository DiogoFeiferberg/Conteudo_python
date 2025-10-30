def calcular_anos_para_ultrapassar(populacao_a, taxa_a, populacao_b, taxa_b):
    """
    Calcula o número de anos para que a população de A ultrapasse a de B.

    Args:
        populacao_a (float): População inicial do país A.
        taxa_a (float): Taxa de crescimento anual do país A (ex: 0.03 para 3%).
        populacao_b (float): População inicial do país B.
        taxa_b (float): Taxa de crescimento anual do país B (ex: 0.015 para 1.5%).

    Returns:
        int: O número de anos necessários, ou None se A nunca ultrapassar B.
    """
    anos = 0
    # Garante que a taxa de crescimento de A seja maior que a de B para que a ultrapassagem ocorra
    if taxa_a <= taxa_b and populacao_a < populacao_b:
        return None  # A nunca ultrapassará B se a taxa de crescimento de A for menor ou igual à de B

    while populacao_a < populacao_b:
        populacao_a *= (1 + taxa_a)
        populacao_b *= (1 + taxa_b)
        anos += 1
    return anos

def obter_entrada_valida(mensagem):
    """
    Obtém uma entrada numérica válida do usuário.

    Args:
        mensagem (str): A mensagem a ser exibida para o usuário.

    Returns:
        float: O número válido inserido pelo usuário.
    """
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            else:
                print("O valor não pode ser negativo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def main():
    while True:
        print("\n--- Calculadora de Crescimento Populacional ---")

        # Permite que o usuário insira as populações e taxas
        populacao_a_inicial = obter_entrada_valida("Digite a população inicial do país A: ")
        taxa_crescimento_a = obter_entrada_valida("Digite a taxa de crescimento anual do país A (ex: 3 para 3%): ") / 100
        populacao_b_inicial = obter_entrada_valida("Digite a população inicial do país B: ")
        taxa_crescimento_b = obter_entrada_valida("Digite a taxa de crescimento anual do país B (ex: 1.5 para 1.5%): ") / 100

        anos = calcular_anos_para_ultrapassar(
            populacao_a_inicial,
            taxa_crescimento_a,
            populacao_b_inicial,
            taxa_crescimento_b
        )

        if anos is None:
            print("O país A nunca ultrapassará o país B com essas taxas de crescimento.")
        else:
            print(f"\nSerão necessários {anos} anos para a população do país A ultrapassar a do país B.")

        # Pergunta se o usuário deseja repetir a operação
        repetir = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if repetir != 's':
            break

if __name__ == "__main__":
    main()