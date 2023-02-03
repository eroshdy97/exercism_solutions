def rotate(text, key):
    small_alpha = 'abcdefghijklmnopqrstuvwxyz'
    capital_alpha = small_alpha.upper()
    output = ''
    for letter in text:
        if letter in small_alpha:
            i = small_alpha.find(letter)
            output += small_alpha[(i + key % 26) % 26]
        elif letter in capital_alpha:
            i = capital_alpha.find(letter)
            output += capital_alpha[(i + key % 26) % 26]
        else:
            output += letter

    return output
