def rows(letter):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in alpha:
        index = alpha.index(letter)

    num_rows = 2 * index + 1

    res = []
    first_last_row = " "*index + "A" + " "*index
    res.append(first_last_row)
    for i in range(index):
        space_sides = index - i - 1
        space_between = num_rows - 2 * (space_sides + 1)
        txt = " " * space_sides + alpha[i+1] + " " * space_between + alpha[i+1] + " " * space_sides
        res.append(txt)
    res += res[-2::-1]

    return res
