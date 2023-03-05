# add "This is the " in the start
# add "." in the end

words = [
        "house that Jack built", # 1

        "malt that lay in the ", # 2

        "rat that ate the ", # 3

        "cat that killed the ", # 4

        "dog that worried the ", # 5

        "cow with the crumpled horn that tossed the ", # 6

        "maiden all forlorn that milked the ", # 7

        "man all tattered and torn that kissed the ", # 8

        "priest all shaven and shorn that married the ", # 9

        "rooster that crowed in the morn that woke the ", # 10

        "farmer sowing his corn that kept the ", # 11

        "horse and the hound and the horn that belonged to the ", # 12
        ]


def recite(start_verse, end_verse):
    ans = []
    for verse in range(start_verse, end_verse + 1):
        res = "."
        for i in range(verse):
            res = words[i] + res
        res = "This is the " + res
        ans.append(res)
    return ans
