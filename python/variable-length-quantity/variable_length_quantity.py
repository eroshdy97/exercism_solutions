import math

def encode(numbers):
    res = []
    for num in numbers:
        mini_res = []
        bin_num = bin(num)
        bin_num = bin_num[2:]
        bin_len = len(bin_num)
        desired_len = math.ceil(bin_len / 7) * 7
        bin_num = "0" * (desired_len - bin_len) + bin_num
        byte = bin_num[-7:]
        bin_num = bin_num[:-7]
        mini_res.append("0" + byte)
        while bin_num:
            byte = bin_num[-7:]
            bin_num = bin_num[:-7]
            mini_res.append("1" + byte)
        mini_res.reverse()
        res = res + mini_res
    res = [(int(x, base=2)) for x in res]
    return res


def decode(bytes_):
    res = []
    mini_res = ''
    for byte in bytes_:
        bin_num = bin(byte)
        bin_num = bin_num[2:]
        if bin_num[0] == 1 or len(bin_num) == 8:
            mini_res = mini_res +  bin_num[-7:]

        if bin_num[0] == 0 or len(bin_num) < 8:
            bin_num = "0" * (7 - len(bin_num)) + bin_num
            mini_res = mini_res +  bin_num
            mini_res = (int(mini_res, base=2))
            res.append(mini_res)
            mini_res = ''
    if res == []:
        raise ValueError("incomplete sequence")
    return res
