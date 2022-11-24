def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if len([x for x in digits if x < 0 or x >= input_base]) > 0:
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    # convert from input_base to base 10
    number = 0
    size = len(digits)
    for i in range(size):
        number += digits[size - 1 - i] * (input_base ** i)

    # convert from base 10 to output_base
    q = number
    r = 0
    result = []
    while number != 0:
        r = number % output_base
        number = number // output_base
        result.append(r)
    
    if result == []:
        return [0]
    else:
        result.reverse()
        return result

