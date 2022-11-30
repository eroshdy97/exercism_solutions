def response(hey_bob):
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        return "Fine. Be that way!"
    elif hey_bob[-1] == "?":
        hey_bob = ''.join([i for i in hey_bob if i.isalpha()])
        if hey_bob == str.upper(hey_bob) and len(hey_bob) > 0:
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    else:
        hey_bob = ''.join([i for i in hey_bob if i.isalpha()])
        if hey_bob == str.upper(hey_bob) and len(hey_bob) > 0:
            return "Whoa, chill out!"
        else:
            return "Whatever."
    
