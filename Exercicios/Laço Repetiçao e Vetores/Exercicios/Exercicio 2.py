while True:
    nome = input('Nome (maior que 3 caracteres): ')
    if len(nome) > 3:
        break
    else:
        print('Nome inválido! Precisa ter mais de 3 caracteres.')

while True:
    try:
        idade = int(input('Idade (entre 0 e 150): '))
        if 0 <= idade <= 150:
            break
        else:
            print('Idade inválida! Precisa ser entre 0 e 150.')
    except ValueError:
        print('Entrada inválida. Por favor, insira um número inteiro.')

while True:
    try:
        salario = float(input('Salário (maior que zero): '))
        if salario > 0:
            break
        else:
            print('Salário inválido! Precisa ser maior que zero.')
    except ValueError:
        print('Entrada inválida. Por favor, insira um número válido para o salário.')

while True:
    estado_civil = input("Estado Civil ('s', 'c', 'v', 'd'): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil inválido! Use 's', 'c', 'v' ou 'd'.")

print('\nInformações válidas:')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: R$ {salario:.2f}')
print(f'Estado Civil: {estado_civil}')

