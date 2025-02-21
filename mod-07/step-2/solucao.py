import random

word_list = ['celular', 'Casa', 'computador']

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Adivine uma letra: ").lower()

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)