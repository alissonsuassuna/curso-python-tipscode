# Desenvolva uma calculadora de IMC usando ás instruções if/elif/else à calculadora deverá 
# interpreta os valores calculados com as seguintes regras:
# Se o IMC estiver abaixo de 18,5 (não incluso), imprima "abaixo do peso"
# # Se o IMC estiver entre 18,5 (inclusive) e 25 (não incluso), imprima "peso normal"
# Se o IMC for 25 (inclusive) ou mais, imprima "acima do peso"
# OBS:

# A fórmula do IMC é:
# weight = 85
# height = 1.85
# bmi = weight / (height ** 2)

peso = float(input('Informe o seu peso atual: '))
altura = float(input('Informe a sua altura: '))

imc = peso / (altura ** 2)
print(imc)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso normal')
else:
    print('Acima do peso')