# Não há escopo de bloco em Python

#if 5 > 2:
#    a_variable = 8

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
       new_enemy = enemies[0]

    print(new_enemy)
