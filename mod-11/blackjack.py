import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Pegar uma lista de cartas e retornar a pontuação calculada com base nas cartas"""
    if sum(cards) == 21 and sum(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "empate"
    elif c_score == 0:
        return "Perdeu, o oponente tem blackjack"
    elif u_score == 0:
        return "Ganhei com um Blackjack"
    elif u_score > 21:
        return "Você passou de 21. Você perdeu"
    elif c_score > 21:
        return "O oponente passou de 21. Você venceu"
    elif u_score > c_score:
        return "Você ganhou"
    else:
        return "Você perdeu"

def play_game():
    print(logo)
    user_cards = []
    computed_cards = []
    computer_score = -1
    use_score = -1
    is_game_over = False


    for _ in range(2):
        user_cards.append(deal_card())
        computed_cards.append(deal_card())

    while not is_game_over:
        use_score = calculate_score(user_cards)
        computer_score = calculate_score(computed_cards)
        print(f"Sua carta é: {user_cards}, pontuação: {use_score}")
        print(f"Primeira carta do Pc: {computed_cards[0]}")

        if use_score == 0 or computer_score == 0 or use_score > 21:
            is_game_over = True
        else:
            use_should_deal = input("Digite 'Y' para pegar outra carta, digite 'N' para passar: ")
            if use_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computed_cards.append(deal_card())
        computer_score = calculate_score(computed_cards)

    print(f"Sua mão final: {user_cards}, pontuação final: {use_score}")
    print(f"A mão final do computador: {computed_cards}, pontuação final: {computer_score}")
    print(compare(use_score, computer_score))

while input("Quer jogar uma partida de blackjack? Digite 'y' sim ou 'n' não: ") == 'y':
    print("\n" * 30)
    play_game()