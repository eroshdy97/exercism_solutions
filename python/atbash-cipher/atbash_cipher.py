def encode(plain_text):
    Plain = "abcdefghijklmnopqrstuvwxyz"
    Cipher = "zyxwvutsrqponmlkjihgfedcba"

    plain_text = plain_text.lower()
    plain_text = plain_text.strip(" ")

    output = ""
    for char in plain_text:
        if char in Plain:
            if (len(output)+1) % 6 == 0:
                output += " "
            index = Plain.index(char)
            output += Cipher[index]
        elif char.isdigit():
            if (len(output)+1) % 6 == 0:
                output += " "
            output += char
    return output

def decode(ciphered_text):
    Plain = "abcdefghijklmnopqrstuvwxyz"
    Cipher = "zyxwvutsrqponmlkjihgfedcba"

    ciphered_text = ciphered_text.lower()
    ciphered_text = ciphered_text.strip(" ")

    output = ""
    for char in ciphered_text:
        if char in Cipher:
            index = Cipher.index(char)
            output += Plain[index]
        elif char.isdigit():
            output += char
    return output

