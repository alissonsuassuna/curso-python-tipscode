# O objetivo é criar um programa Python de entrega de pizza, e o programa calcula automaticamente 
# a conta para o usuário com base em várias opções

# Tabela de pizza

# Pizza pequena - R$15 Reais
# Pizza média - R$20 Reais
# Pizza grande - R$25Reais

# Adiciona pepperoni na pizza pequena + R$2 reais
# Adiciona pepperoni na pizza médio e grande + R$3 reais
# Queijo extra em todos os tamanho (Sim ou não) + R$1 Real

print('Seja bem-vindo a pizzaria TipsCode!')
size = input('Qual tamanho da pizzar? (P) pequena, (m) média, (L) grande: ')
pepperoni = input('Deseja adicionar pepperoni (S) Sim, (N) Não? ')
extra_cheese = input('Deseja com queijo (s) Sim, (n) Não ')

bill = 0

if size == 'p':
    bill += 15
elif size == 'm':
    bill += 20
elif size == 'l':
    bill += 25
else:
    print('Seleção de campo inválida')
    
if pepperoni == 's':
    if size == 'p':
        bill += 2
    else:
        bill += 3
        
if extra_cheese == 's':
    bill += 1
    
print(f'Valor final da pizza é: R${bill}')