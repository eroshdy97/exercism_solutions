from random import randint, random


def private_key(p):
    a = randint(2, p-1)
    return a


def public_key(p, g, private):
    A = (g ** private) % p
    return A


def secret(p, public, private):
    s = (public ** private) % p
    return s
