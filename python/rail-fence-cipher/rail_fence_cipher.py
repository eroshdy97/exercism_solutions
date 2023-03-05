def encode(message, rails):
    message = message.strip(" ")
    rails_mat = [""] * rails
    down:bool = True
    n = 0
    for char in (message):
        if down:
            rails_mat[n] += char
            n += 1
            if n == rails:
                down = False
                n -= 2
        
        else:
            rails_mat[n] += char
            n -= 1
            if n == -1:
                down = True
                n += 2

    return "".join(rails_mat)


'''
W . . . E . x . C . . . R . . . L . x . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . x . I . x . V . . . D . x . E . x . N . .
. . . x . . . . . x . . . . . x . . . . . x . . .
'''
def decode(encoded_message, rails):
    res = [""] * rails
    nums = [0] * rails
    msg_len = len(encoded_message)

    down:bool = True
    n = 0
    for i in range(msg_len):
        if down:
            nums[n] += 1
            n += 1
            if n == rails:
                down = False
                n -= 2
        
        else:
            nums[n] += 1
            n -= 1
            if n == -1:
                down = True
                n += 2
    print(nums)
    for rail in range(rails):
        res[rail] = encoded_message[:nums[rail]]
        encoded_message = encoded_message[nums[rail]:]
        print(res[rail])

    out = ""
    down:bool = True
    n = 0
    for i in range(msg_len):
        if down:
            out += res[n][0]
            res[n] = res[n][1:] if len(res[n]) > 1 else ""
            n += 1
            if n == rails:
                down = False
                n -= 2
        
        else:
            out += res[n][0]
            res[n] = res[n][1:] if len(res[n]) > 1 else ""
            n -= 1
            if n == -1:
                down = True
                n += 2

    return out


