# Local Scope

# Global Scope
player_health = 10

# Namespaces
def game():
    def drink_potion():
       potion_strength = 2
       print(player_health)


drink_potion()

#print(f"depois da função {player_health}")