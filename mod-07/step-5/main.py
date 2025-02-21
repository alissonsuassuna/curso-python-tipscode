import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"*******************{lives}/6 vidas restantes *******************")
    guess = input("Adivine uma letra: ").lower()

    if guess in correct_letters:
        print(f"Você já adivinhou essa letra {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"você adivinhou {guess}, essa letra não está na palavra. Você perderá uma vida")

        if lives == 0:
            game_over = True
            print(f"******************* A palavra é {chosen_word}! Você perdeu! *******************")

    if "_" not in display:
        game_over = True
        print('Você venceu')

    print(stages[lives])