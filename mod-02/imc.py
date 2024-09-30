# Neste aula, vamos escrever um programa que calcula o Índice de Massa 
#Corporal de alguém, usando o peso e altura do usuário.

# Abaixo da aula, você verá um link para a página da Wikipedia sobre IMC.

# https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal

altura = float(input('digite sua altura: '))

peso = float(input('digite seu peso: '))

imc = peso / (altura * altura)

novo_imc = int(imc)

print('seu imc é: ' + str(novo_imc))