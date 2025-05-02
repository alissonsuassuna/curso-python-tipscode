#TODO-1: Peça a contribuição do usuário
#TODO-2: Salvar os dados no dicionario {name: price}
#TODO-3: Se novos lances precisam ser adicionados
#TODO-4: Comparar lances no dicionário

def compare_leilao(bidding_dictionary):
    winner = ""
    higest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > higest_bid:
            higest_bid = bid_amount
            winner = bidder

    print(f"Vencedor é {winner} com o lance de R${higest_bid}")

bids = {}
should_bidding = True

while should_bidding:
    name = input("Digite seu nome!")
    price = int(input("Qual é o valor do seu lance?: R$ "))
    bids[name] = price
    should_continue = input("Há outros licitantes? Digite 'YES' ou 'No' \n").lower()

    if should_continue == 'no':
        should_bidding = False
        compare_leilao(bids)
    elif should_continue == "yes":
        print("\n" * 100)

