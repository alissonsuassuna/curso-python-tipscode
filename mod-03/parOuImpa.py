# Escreva um programa em python onde o cliente vai digitar um número
# qualquer e retorne se esse número digitado é PAR ou ÍMPAR?

numero_a_verificar = int(input('Digite um número: '))

print(numero_a_verificar % 2)

if numero_a_verificar % 2 == 0:
    print('O número é PAR')
else:
    print('O número é ÍMPA')