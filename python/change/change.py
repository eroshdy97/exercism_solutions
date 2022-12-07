def min_change_table(V, C):
    m, n = C+1, len(V)
    table, solution = [0] * m, [0] * m
    for i in range(1, m):
        minNum, minIdx = float('inf'), -1
        for j in range(n):
            if V[j] <= i and 1 + table[i - V[j]] < minNum:
                minNum = 1 + table[i - V[j]]
                minIdx = j
        table[i] = minNum
        solution[i] = minIdx
    return (table, solution)


def find_fewest_coins(V, C):
    if C == 0:
        return []
    if C < 0:
        raise ValueError("target can't be negative")
    if len(V) < 1 or C < V[0]:
        raise ValueError("can't make target with given coins")


    table, solution = min_change_table(V, C)
    num_coins, coins = table[-1], []
    if num_coins == float('inf'):
        raise ValueError("can't make target with given coins")
    while C > 0:
        coins.append(V[solution[C]])
        C -= V[solution[C]]
    return coins

