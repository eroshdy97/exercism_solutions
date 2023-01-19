def is_pangram(sentence):
    sentence = sentence.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    correct = True
    for letter in alpha:
        if letter not in sentence:
            correct = False
            break

    return correct
