import random

word_list = ['celular', 'Casa', 'computador']

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input('Adivinhe ima letra: ').lower()

for letter in chosen_word:
    if letter == guess:
        print("Certo")
    else:
        print('Errado')
