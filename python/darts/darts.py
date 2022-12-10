from logging import root


def score(x, y):
    Rout = 10
    Rmid = 5
    Rin = 1
    d = ((x**2)+(y**2))**0.5
    if d > Rout :
        return 0
    elif d > Rmid:
        return 1
    elif d > Rin:
        return 5
    else:
        return 10
