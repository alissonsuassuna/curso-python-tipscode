# No Brasil é bem comum jogar um jogo chamado amigo secreto, normalmente esse jogo é feito em festas de fim de ano.

# Sempre fazemos esse jogo, existem tbm algumas variações como o amigo doce.

# O jogo funciona da seguinte forma: é feito uma lista com os nomes dos participantes e é feito um sorteio onde cada pessoa tira um nome aleatório.

# Com base nisso, como somos programadores vamos criar um algoritmo que faça esse sorteio de nomes de forma totalmente aleatória.
import random

friends = ['Jesus Cristo', 'Elias', 'Maria', 'João Batista', 'Davi', 'Paulo', 'Pedro']


print(random.choice(friends))