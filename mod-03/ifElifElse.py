print('Seja bem-vindo(a) ao TipsPark')

altura = int(input('Qual é a sua altura? '))
conta = 0

if altura >= 120:
    print('Vende o ingresso!')
    idade = int(input('Qual é a sua idade? '))
    if idade <= 12:
        conta = 55
        print('O ingresso vai custar R$5 Reais')
    elif idade <= 18:
        conta = 12
        print('O ingresso vai custar R$12')
    else:
        conta = 24
        print('O ingresso vai custar R$24 Reais')
        
    photo = input('Deseja tirar foto? Sim (s), Não (n)')
    if photo == 's':
        conta += 3
    
    print(f'Sua conta final é R${conta}')
else:
    print('Lamento você não vai!')