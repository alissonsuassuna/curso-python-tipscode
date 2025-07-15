try:
    age = int(input("Quantos anos você tem"))
except ValueError:
    print("Você digitou um valor não suportado, por favor digite novamente")
    age = int(input("Quantos anos você tem"))
if age > 18:
    print(f"Você pode dirigir aos {age} anos")