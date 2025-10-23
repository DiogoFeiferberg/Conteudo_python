print("M - Masculino | F - Feminino | O - Outros")
sexo =input('Digite a letra correspondente ao seu sexo:  ')
if sexo == "M" or sexo == "m":
    print("Voce é do sexo Masculino")
elif sexo == "F" or sexo == "f":
    print("Voce é do sexo Feminino")
else:
    print("Voce preferiu nao informar")
match sexo:
    case "M":
        print("Sexo Masculino")
    case "m":
        print("Sexo Masculino")
    case "F":
        print("Sexo Feminino")
    case "f":
        print("Sexo Feminino")
    case _:
        print("Undefined")