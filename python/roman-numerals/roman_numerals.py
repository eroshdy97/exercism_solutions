'''
 1       => I
 5       => V
 10      => X
 50      => L
 100     => C
 500     => D
 1000    => M
'''

def encode_num(num :int):
    res = ""
    if num == 1:
        res = "I"
    elif num == 2:
        res = "II"
    elif num == 3:
        res = "III"
    elif num == 4:
        res = "IV"
    elif num == 5:
        res = "V"
    elif num == 6:
        res = "VI"
    elif num == 7:
        res = "VII"
    elif num == 8:
        res = "VIII"
    elif num == 9:
        res = "IX"
    else:
        raise ValueError("num is wrong!")
    return res


def upgrade_num(num :str, pos :int):
    res = ""
    tens = ["I", "X", "C", "M"]
    fives = ["V", "L", "D"]

    for char in num:
        if char in tens:
            i = tens.index(char)
            res += tens[pos-1+i]
        elif char in fives:
            i = fives.index(char)
            res += fives[pos-1+i]
        else:
            raise ValueError("wrong letter")
        
    return res

    
def roman(number):
    res = ""
    str_number = str(number)
    length = len(str_number)

    for i, digit in enumerate(str_number):
        if digit == '0':
            continue

        d = int(digit)
        encoded_digit = encode_num(d)
        upgraded_digit = upgrade_num(encoded_digit, length - i)
        res += upgraded_digit
    
    return res
