'''
1 2     1 2 3       1  2  3  4      1  2  3  4  5
4 3     8 9 4       12 13 14 5      16 17 18 19 6
        7 6 5       11 16 15 6      15 24 25 20 7
                    10 9  8  7      14 23 22 21 8
                                    13 12 11 10 9
'''
def change_dir(x, y, d):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    x -= dirs[d][0]
    y -= dirs[d][1]
    d = (d+1)%4
    x += dirs[d][0]
    y += dirs[d][1]
    return x, y, d

def spiral_matrix(size):
    max_elem = size * size
    all_nums = [i+1 for i in range(max_elem)]
    mat = [[0 for i in range(size)] for i in range(size)]

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    d = 0
    x, y = 0, 0
    num = 0
    for num in all_nums:
        print("number = ", num, "\t(x, y) = (", x, ", ", y, ")")
        mat[y][x] = num
        x += dirs[d][0]
        y += dirs[d][1]
        if x >= size or y >= size or x < 0 or y < 0:
            x, y, d = change_dir(x, y, d)
        elif mat[y][x] in all_nums:
            x, y, d = change_dir(x, y, d)

    return mat
