def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    vowels2 = ['xr', 'yt']

    words = text.split()

    for i, word in enumerate(words):
        if word[0] in vowels[:-1] or word[0]+word[1] in vowels2:
            words[i] = words[i]+ "ay"

        else:
            has_vowel = False
            for j, letter in enumerate(word):
                if letter in vowels:
                    if j >= 1 and word[j-1]+word[j] == 'qu':
                        words[i] = word[j+1:] + word[:j+1] + "ay"
                    elif letter == 'y' and j == 0:
                        continue
                    else:
                        words[i] = word[j:] + word[:j] + "ay"
                    
                    has_vowel = True
                    break

            if(has_vowel == False):
                words[i] = words[i]+ "ay"

    return ' '.join(words)
