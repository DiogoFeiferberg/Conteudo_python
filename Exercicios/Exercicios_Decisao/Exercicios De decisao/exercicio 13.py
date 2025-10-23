numero = -1

while numero == -1:
    numero = int(input("Digite um número de 1 a 7: "))
    if numero < 1 or numero > 7:
        numero = -1
        print("Número inválido")


if numero == 1:
  print("Domingo")
elif numero == 2:
  print("Segunda-feira")
elif numero == 3:
  print("Terça-feira")
elif numero == 4:
  print("Quarta-feira")
elif numero == 5:
  print("Quinta-feira")
elif numero == 6:
  print("Sexta-feira")
elif numero == 7:
  print("Sábado")