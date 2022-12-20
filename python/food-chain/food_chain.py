def recite(start_verse, end_verse):
    first = "I know an old lady who swallowed a "
    last = "I don't know why she swallowed the fly. Perhaps she'll die."
    animals = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]
    customs = [
        [], # fly
        "It wriggled and jiggled and tickled inside her.", # spider
        "How absurd to swallow a bird!", # bird
        "Imagine that, to swallow a cat!", # cat
        "What a hog, to swallow a dog!", # dog
        "Just opened her throat and swallowed a goat!", # goat
        "I don't know how she swallowed a cow!", # cow
        "She's dead, of course!" # horse
    ]

    ans = []

    for verse in range(start_verse, end_verse+1):
        ans.append("")
        txt = first + animals[verse-1] + "."
        ans.append(txt)
        if verse != 1:
            ans.append(customs[verse-1])
        if verse == 8:
            continue
        for i in range(verse-1, 0, -1):
            txt = "She swallowed the " + animals[i]
            txt += " to catch the " + animals[i-1]
            txt += " that wriggled and jiggled and tickled inside her." if i == 2 else "."
            ans.append(txt)
        ans.append(last)

    return ans[1:]
