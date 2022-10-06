alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.



def caesar(text, shift, direction):
    cipherText = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter == " ":
            cipherText += " "
        else:
            position = alphabet.index(letter)
            newPosition = position + shift
            cipherText += alphabet[newPosition]
    print(f"The {direction}d text is {cipherText}")



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(text, shift, direction)