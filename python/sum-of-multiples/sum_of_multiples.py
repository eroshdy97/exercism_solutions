def sum_of_multiples(limit, multiples):
    all_nums = list(range(limit))
    ans = set()
    for div in multiples:
        if div == 0:
            continue
        val = [x for x in all_nums if x % div == 0]
        ans.update(val)
    return sum(ans)
