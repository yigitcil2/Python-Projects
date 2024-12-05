import caesar_cypher_art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']
print(caesar_cypher_art.logo)


def caesar(original_text, shift_amount, user_choice):

    if user_choice =='e':
        cipher_text = ""
        for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position = shifted_position % len(alphabet)
            cipher_text += alphabet[shifted_position]
        print(f"Encoded result: {cipher_text}")
    elif user_choice =='d':
        decoded_text = ""
        for letter in original_text:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position = shifted_position % len(alphabet)
            decoded_text += alphabet[shifted_position]
        print(f"Decoded result: {decoded_text}")

system_continue = True
while system_continue:
    choice = input("Would you like to encode or decode the text? \ne for encode \nd for decode")
    text = input("Insert message: ")
    shift = int(input("Insert shift: "))
    caesar(original_text=text, shift_amount=shift, user_choice=choice)

    continue_input = input("Continue to system? y / n")
    if continue_input == 'y':
        system_continue = True
    elif continue_input == 'n':
        system_continue = False

