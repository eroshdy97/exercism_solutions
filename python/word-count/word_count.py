def count_words(sentence :str):
    punc = '''!()-[]{};:"\,<>./?@#$%^&*_~'''

    sentence = sentence.lower()
    for index, char in enumerate(sentence):
        if char in punc:
            sentence = sentence.replace(char, " ")            
        
    spl = sentence.split()
    for i, word in enumerate(spl):
        newword = word
        while newword and not newword[-1].isalnum():
            newword = newword[:-1]
        while newword and not newword[0].isalnum():
            newword = newword[1:]
        spl[i] = newword

    spl = [x for x in spl if len(x) > 0]
    ans = dict()
    for word in spl:
        if word.lower() in ans:
            ans[word.lower()] += 1
        else:
            ans[word.lower()] = 1
    
    return ans
