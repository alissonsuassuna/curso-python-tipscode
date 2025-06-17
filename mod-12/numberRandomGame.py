from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def check_answer(user_guess, actual_answer, turns):
    """Verifica a resposta contra o papite e retorna o número de palpites restantes"""
    if user_guess > actual_answer:
        print("Muito alto")
        return  turns - 1
    elif user_guess < actual_answer:
        print("Muito baixo")
        return  turns - 1
    else:
        print(f"Você acertou! A resposta foi {actual_answer}")

def set_difficulty():
    level = input("Qual é o nível de dificuldade? Digite 'fácil' ou 'difícil '")
    if level == "fácil":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Seja bem-vindo ao jogo de adivinhação")
    print("Estou pensando em um número de 1 a 100!")
    answer = randint(1, 100)

    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"Você tem {turns} tentativas restante para adivinha!")
        guess = int(input("Qual é o seu palpite: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Você ficou sem palpites, você perdeu")
            return
        elif guess != answer:
            print("Adivinha novamente")

game()
