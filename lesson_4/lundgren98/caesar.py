
lower = "abcdefghijlkmnopqrstuvwxyzåäö"
upper = "ABCDEFGHIJLKMNOPQRSTUVWXYZÅÄÖ"

def shift_char(character, shift):
    if character in lower:
        alphabet = lower
    elif character in upper:
        alphabet = upper
    else:
        return character
    new_character_index = alphabet.index(character) + shift
    return alphabet[new_character_index % len(alphabet)]

def encrypt(msg, shift):
    encrypted_msg = ""
    for c in msg:
        encrypted_msg += shift_char(c, shift)
    return encrypted_msg

if __name__ == '__main__':
    shift = int(input('How many shifts do you want? '))
    msg = input('Type your secret message: ')
    msg = encrypt(msg, shift)
    print(f'This is your encrypted message:\n\t{msg}')
