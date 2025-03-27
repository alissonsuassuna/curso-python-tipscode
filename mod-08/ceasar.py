import art

print(art.logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ''

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            # 25
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Decodificado: {output_text}" if encode_or_decode == "decode" else f"Codificado: {output_text}")

should_continue = True

while should_continue:

    direction = input("Digite 'encode' para criptografar, digite 'decode' para descriptografar:\n").lower()
    text = input("Digite sua mensagem\n").lower()
    shift = int(input("Digite o número do deslocamento\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Se deseja continuar digite YES. Caso não digite NO.\n").lower()
    if restart == 'no':
        should_continue = False
        print("O programa foi encerrado!")
