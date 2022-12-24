def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)


def total():
    total = 0
    for num in range(1, 65):
        total += 2 ** (num-1)
    return total
