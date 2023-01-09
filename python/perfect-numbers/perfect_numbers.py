from curses.ascii import isdigit


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    output = sum(divisor for divisor in range(1, number // 2 + 1) if number % divisor == 0)

    if output == number:
        return "perfect"
    elif output > number:
        return "abundant"
    else :
        return "deficient"
    