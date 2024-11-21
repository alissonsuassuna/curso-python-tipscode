import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input('Quantas letras você deseja em sua senha?: \n'))
nr_symbols = int(input('Quantos simbolos você deseja?:\n '))
nr_numbers = int(input('Quantos números você deseja?:\n'))

# Facil
# password = ''
#                        #= 4 0 1 2 3
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(password)
#

# Hard
password_list = []
                       #= 4 0 1 2 3
for char in range(0, nr_letters):
    password_list += random.choice(letters)

for char in range(0, nr_symbols):
    password_list += random.choice(symbols)

for char in range(0, nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ''
for char in password_list:
    password += char

print(f'Sua nova senha é: {password}')