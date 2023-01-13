def is_isogram(string):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    for letter in string:
        if letter in alpha and string.count(letter) > 1:
            return False
    
    return True
