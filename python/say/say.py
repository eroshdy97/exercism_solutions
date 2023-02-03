def encode_0_9(num :int):
    res = ""
    if num == 0:
        res = "zero"
    elif num == 1:
        res = "one"
    elif num == 2:
        res = "two"
    elif num == 3:
        res = "three"
    elif num == 4:
        res = "four"
    elif num == 5:
        res = "five"
    elif num == 6:
        res = "six"
    elif num == 7:
        res = "seven"
    elif num == 8:
        res = "eight"
    elif num == 9:
        res = "nine"
    return res

def encode_10_19(num :int):
    if num == 10:
        return "ten"
    elif num == 11:
        return "eleven"
    elif num == 12:
        return "twelve"
    elif num == 13:
        return "thirteen"
    elif num == 14:
        return "fourteen"
    elif num == 15:
        return "fifteen"
    elif num == 16:
        return "sixteen"
    elif num == 17:
        return "seventeen"
    elif num == 18:
        return "eighteen"
    elif num == 19:
        return "ninteen"

def encode_20_90(num :int):
    if num == 20:
        return "twenty"
    elif num == 30:
        return "thirty"
    elif num == 40:
        return "forty"
    elif num == 50:
        return "fifty"
    elif num == 60:
        return "sixty"
    elif num == 70:
        return "seventy"
    elif num == 80:
        return "eighty"
    elif num == 90:
        return "ninety"

def encode_2_digits(num :str):
    mini_res = ""
        
    if num[0] == "1":
        mini_res = encode_10_19(int(num))
    else:
        mini_res = encode_20_90(int(num[0] + "0"))
        if num[0] == "0" and num[1] != "0":
            mini_res = encode_0_9(int(num[1]))
        elif num[1] != "0":
            check = encode_0_9(int(num[1]))
            mini_res = mini_res + "-" + check if check else ""
    return mini_res


def say(number): # 0 to 999,999,999,999
    if number > 999_999_999_999 or number < 0:
        raise ValueError("input out of range")

    res = ""
    num_str = str(number)
    num_arr = []

    while num_str:
        num_arr.append(num_str[-3:])
        num_str = num_str[:-3]

    endings = ["", " thousand", " million", " billion"]
    for index, num in enumerate(num_arr):
        mini_res = ""
        if len(num) == 1:
            mini_res = encode_0_9(int(num))
        elif len(num) == 2:
            mini_res = encode_2_digits(num)
        elif len(num) == 3:
            if num == "000":
                continue
            mini_res = encode_0_9(int(num[0])) + " hundred " if encode_0_9(int(num[0])) != "zero" else ""
            check = encode_2_digits(num[1:])
            mini_res += check if check  else ""
        
        mini_res += endings[index]
        res = mini_res + " " + res
    return res.strip()

