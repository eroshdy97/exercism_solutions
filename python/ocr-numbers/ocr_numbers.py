def get_number(number):
    row1, row2, row3, row4 = number

    if row1 == " _ " and row2 == "| |" and row3 == "|_|":
        return "0"

    elif row1 == "   " and row2 == "  |" and row3 == "  |":
        return "1"

    elif row1 == " _ " and row2 == " _|" and row3 == "|_ ":
        return "2"

    elif row1 == " _ " and row2 == " _|" and row3 == " _|":
        return "3"

    elif row1 == "   " and row2 == "|_|" and row3 == "  |":
        return "4"

    elif row1 == " _ " and row2 == "|_ " and row3 == " _|":
        return "5"

    elif row1 == " _ " and row2 == "|_ " and row3 == "|_|":
        return "6"

    elif row1 == " _ " and row2 == "  |" and row3 == "  |":
        return "7"

    elif row1 == " _ " and row2 == "|_|" and row3 == "|_|":
        return "8"

    elif row1 == " _ " and row2 == "|_|" and row3 == " _|":
        return "9"

    else:
        return "?"

def convert(input_grid):
    ans = ""
    height = len(input_grid)
    width = len(input_grid[0])

    if height % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if width % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    row_num = height // 4
    column_num = width // 3

    for row in range(row_num):
        res = ""
        for col in range(column_num):
            num = []
            num.append(input_grid[4*row + 0][3*col: 3*col + 3])
            num.append(input_grid[4*row + 1][3*col: 3*col + 3])
            num.append(input_grid[4*row + 2][3*col: 3*col + 3])
            num.append(input_grid[4*row + 3][3*col: 3*col + 3])
            res += get_number(num)
        ans = ans + res + ","

    ans = ans[:-1] if len(ans) > 0 else ans
    return ans

