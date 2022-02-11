#Create a Ceasar Cipher
# https://en.wikipedia.org/wiki/Caesar_cipher

#Made easier using Ascii Code
#Right shift
def encrypt(text, shifts):
    encrypt_word = ""
    for c in text:
        if c != " ":
            encrypt_word += chr(ord(c)+shifts)
        else:
            encrypt_word += c

    print(f"The encoded text is: {encrypt_word}")


#Left Shift
def decrpyt(encWord, shifts):
    decrpyt_word = ""
    for c in encWord:
        if c != " ":
            decrpyt_word += chr(ord(c)-shifts)
        else:
            decrpyt_word += c

    print(f"The decoded text is: {decrpyt_word}")


run = True

while run:
    direction = input("Type \'encode\' to encrypt  or \'decode\' to decrypt:\n ").casefold()
    text = input("Type your message: \n")
    shifts = int(input("Type number of shifts: "))
    if direction == "encode":
        encrypt(text, shifts)
    elif direction == "decrypt":
        decrpyt(encWord=text, shifts=shifts)
    
    direction = input("Type \"yes\" if you want to go again. Otherwise type \"no\".").casefold()
    if direction == "no":
        run = False

