enemies = 1

def increase_enemies(enemies):
    print(f"inimigos dentro da função: {enemies}")
    return enemies

enemies = increase_enemies(enemies)
print(f"inimigos fora da função: {enemies}")