from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("Digite o primeiro nomero: "))

    while should_accumulate:

        for symbol in operation:
            print(symbol)

        # TODO 03: Pergunte ao usuário qual dessas operações ele deseja fazer?
        operation_symbol = input("Qual é a operação? ")
        # TODO 04: Solicite o segundo número ao usuário?
        num2 = float(input("Digite o segundo nomero: "))
        answer = operation[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Digite 'y' para continuar calculando com {answer} ou digite 'n' para iniciar um novo cálculo")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 30)
            calculator()

calculator()