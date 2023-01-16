def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor < min_factor:
        raise ValueError("min must be <= max")

    lst = list(range(min_factor, max_factor + 1))
    lst.reverse()

    product = None
    rev_product = 0
    found :bool = False
    factors = []
    for i in lst:
        for j in lst[lst.index(i):]:
            if not found:
                product = i * j
                rev_product = int(str(product)[::-1])
                if product == rev_product:
                    found = True
                    factors.append([i, j])
                else:
                    product = None

            else:
                if i * j > product:
                    temp = i * j
                    rev_product = int(str(temp)[::-1])
                    if temp == rev_product:
                        factors.clear()
                        factors.append([i, j])
                        product = temp


                elif i * j == product:
                    factors.append([i, j])

    return (product, factors)
            

def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor < min_factor:
        raise ValueError("min must be <= max")

    lst = list(range(min_factor, max_factor + 1))

    product = None
    rev_product = 0
    found :bool = False
    factors = []
    for i in lst:
        for j in lst[lst.index(i):]:
            if not found:
                product = i * j
                rev_product = int(str(product)[::-1])
                if product == rev_product:
                    found = True
                    factors.append([i, j])
                else:
                    product = None

            else:
                if i * j == product:
                    factors.append([i, j])

    return (product, factors)
