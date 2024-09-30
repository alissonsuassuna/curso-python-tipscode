# Neste exercício, o objetivo é escrever um programa que 
# some um número de dois dígitos.

# Terá um input onde você vai extrair os dois números
# do mesmo input
#Exemplo 3 + 9 = 12

entrada = input('Digite um valor com 2 digitos: ')

num1 = int(entrada[0])
num2 = int(entrada[1])

newNumber = num1 + num2

print(newNumber)
