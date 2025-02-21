import random

word_list = ['celular', 'casa', 'computador']

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ''
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += '_'

print(placeholder)

game_over = False
corrent_letter = []

while not game_over:

    guess = input("Adivine uma letra: ").lower()
    print(guess)

    display = ''

    #TODO-2: Altere o loop for para que você mantenha a letra adivinhada anteriomente.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            corrent_letter.append(letter)
        elif letter in corrent_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print('Você vendeu')