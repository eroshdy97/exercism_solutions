def saddle_points(matrix):
    if len(matrix) < 1:
        return []
    ans = []
    row_len = len(matrix[0])
    for row_index, row in enumerate(matrix):
        if len(row) != row_len:
            raise ValueError("irregular matrix")
        max_ele = max(row)
        col_index = [i for i, v in enumerate(row) if v == max_ele]
        for j in col_index:
            saddle :bool = True
            for i in range(len(matrix)):
                if matrix[i][j] < max_ele:
                    saddle = False
                    break
            if saddle:
                ans.append({'row': row_index+1, 'column': j+1})
        
    return ans