print('Seja bem-vindo(a) ao APP Gorjeta')

conta = float(input('Informe o valor da conta R$: '))

porcentagem = int(input('que porcentagem de gorjeta você gostaria de dar? 10%, 12%, ou 15%? '))

pessoas = int(input('Quantas pessoas irá pagar? '))

contaComGorjeta = porcentagem / 100 * conta + conta

valor_total = contaComGorjeta / pessoas

print(valor_total)