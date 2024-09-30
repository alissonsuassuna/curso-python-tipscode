# Nesta atividade vamos escrever um programa que irá calcular em média quantas semanas de vida lhe resta aqui na terra.

# O objetivo é considerar a entrada de acordo com a sua idade.

# Por exemplo, aqui tenho alguém de 15 anos, e presumimos que ele viverq até os 90, seremos otimistas.

# E então vamos calcular quantas semanas ainda restam em sua vida.

age = int(input('Quantos anos você tem?'))


years = 90 - age
weeks = years * 52
print(f'Você ainda tem {weeks} semanas de vida')