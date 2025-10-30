while True:
    nota = float(input("Informe uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        break  
    else:
        print("Nota inválida. Por favor, insira um valor entre 0 e 10.")

print(f"Nota válida informada: {nota}")





