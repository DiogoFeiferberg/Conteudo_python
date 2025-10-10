# operadores matematicos
import math

# + <- soma: soma o valor da esquerda com o da direita
# - <- subtraçao:subtrai o valor da esquerda pelo da direita
# * <- Multiplicaçao: multiplica o valor da esquerda com o da direita
# / <- Divisao:Divide o valor da esquerda pelo da direita

# ** <- potencia: Eleva o valor da esquerda pelo da direita

# Math.sqrt(valor) <- Raiz quadrada:Tira a raiz quadrada do valor
# // <- Inteira da divisao:quando faz uma divisao que resulta em
# valor float,retorna so a parte inteira.10.56 retornaria apenas 10

# % <- resto da divisao:retorna o valor de resto quando a divisao
# nao e exata. 5/2 teria o resto 1.Util na identificaçao de valores par

valor_1 = int(input('Digite o valor 1: '))
valor_2 = int(input('Digite o valor 2: '))

print ("Os valores digitados sao",valor_1,"e",valor_2)

resultado = valor_1 + valor_2

print("a soma dos dois valores é",resultado)

resultado = valor_1 - valor_2
print("A subtraçao dos dois valores é",resultado)

resultado = valor_1 / valor_2
print("A divisao dos dois valores é",resultado)

resultado = valor_1 ** valor_2
print('A potencia dos dois valores é',resultado)

resultado = valor_1 * valor_2
print("a multiplicaçao dos dois valores é",resultado)

resultado = valor_1 // valor_2
print("a divisao inteira dos dois valores é",resultado)

resultado = valor_1 % valor_2
print("o resto da divisao dos dois valores é",resultado)

resultado = math.sqrt (valor_1)
print("A raiz quadrada de",valor_1,"é",resultado)

print("o valor de PI é",math.pi)







