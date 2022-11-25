def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    total = [x ** len(digits) for x in digits]
    total = sum(total)
    return number == total
