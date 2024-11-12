import random

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''


tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)


'''


pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___

'''

game_images = [pedra, papel, tesoura]

user_choise = int(input('Qual é a opção que você deseja? (0) Pedra, (1) Papel, (2) Tesoura! \n'))

if user_choise >= 0 and user_choise <= 2:
    print(game_images[user_choise])

computer_choice = random.randint(0, 2)

print('Computador')
print(game_images[computer_choice])

if user_choise >= 3 or user_choise < 0:
    print('Você digitou uma opção inválida')
elif user_choise == 0 and computer_choice == 2:
    print('Você ganhou')
elif computer_choice == 0 and user_choise == 2:
    print('Você perdeu')
elif computer_choice > user_choise:
    print('Você perdeu')
elif user_choise > computer_choice: 
    print('Você ganhou')
elif computer_choice == user_choise:
    print('Empate!')
elif user_choise >= 3 or user_choise < 0:
    print('Você digitou uma opção inválida')