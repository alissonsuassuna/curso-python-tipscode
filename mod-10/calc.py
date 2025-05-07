def add(n1, n2):
    return n1 + n2

# TODO 01: Escreva ás outras três funções - subtrair(), multiplicar() e dividir()
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO 02: Adicionar estas 4 funções a um dicionário como valores. Chave = "+", "-", "*", "/"
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO 03: Use as operações do dicionário para realizar os cálculos. Multiplique 4 * 8 usando o dicionário.
print(operation["*"](4, 8))