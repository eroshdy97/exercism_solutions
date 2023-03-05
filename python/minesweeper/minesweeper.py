def annotate(minefield):
    # Function body starts here
    check = [len(x) for x in minefield]
    if len(minefield) > 0 and  sum(check) / len(minefield) != len(minefield[0]):
        raise ValueError("The board is invalid with current input.")
    
    matrix = [list(x) for x in minefield]
    for row_index, row in enumerate(matrix):
        for char_index, char in enumerate(row):
            if char != " " and char != "*":
                raise ValueError("The board is invalid with current input.")
            
            
    for row_index, row in enumerate(matrix):
        for char_index, char in enumerate(row):
            if char == "*":
                for y in range(max(row_index-1, 0), min(len(matrix), row_index+2)):
                    for x in range(max(char_index-1, 0), min(len(matrix[row_index]), char_index+2)):
                        if matrix[y][x] == '*':
                            continue
                        elif matrix[y][x] == ' ':
                            matrix[y][x] = '1'
                        else:
                            num = matrix[y][x]
                            num = int(num)
                            num += 1
                            num = str(num)
                            matrix[y][x] = num

    minefield = ["".join(x) for x in matrix]
    return minefield  

                                                    
                    
