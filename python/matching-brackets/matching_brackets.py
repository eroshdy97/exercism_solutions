def is_paired(input_string):
    left_symbols = ['(', '{', '[']
    right_symbols = [')', '}', ']']
    symbols_output = [0, 0, 0] # () {} []
    last_symbol = ''

    for char in input_string:
        if char == left_symbols[0]:
            symbols_output[0] += 1
            last_symbol += char

        if char == left_symbols[1]:
            symbols_output[1] += 1
            last_symbol += char

        if char == left_symbols[2]:
            symbols_output[2] += 1
            last_symbol += char


        if char == right_symbols[0]: # {(})
            symbols_output[0] -= 1
            if symbols_output[0] < 0 or last_symbol[-1] != left_symbols[0]:
                return False
            else:
                last_symbol = last_symbol[:-1]

        if char == right_symbols[1]:
            symbols_output[1] -= 1
            if symbols_output[1] < 0 or last_symbol[-1] != left_symbols[1]:
                return False
            else:
                last_symbol = last_symbol[:-1]
                

        if char == right_symbols[2]:
            symbols_output[2] -= 1
            if symbols_output[2] < 0 or last_symbol[-1] != left_symbols[2]:
                return False
            else:
                last_symbol = last_symbol[:-1]
                

    return len(last_symbol) == 0
