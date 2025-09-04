print("! Pokemon Name ! Type !")
print("------------------------")

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Nome Pokemon", ["Pikachu", "Squirtle", "Charmander"])

table.add_column("Tipo", ["Electric", 'Water', "Fire"])

table.align = 'l'
print(table)
