def primes(limit):
    all_nums = set(range(2, limit+1))
    ans = []
    for num in all_nums:
        ans.append(num)
        subset :set = set([x for x in all_nums if x % num == 0 and x != num])
        all_nums = all_nums.difference(subset)
        print(all_nums)
    return sorted(list(all_nums))