def triplets_with_sum(n):
    ans = []
    for a in range(1, n//2):
        b = (n/2) * (n-2*a) / (n-a)
        if a >= b:
            break
        print("a: ", a, " b: ", b, " c: ", n-a-b)
        if b == int(b):
            ans.append([a, int(b), int(n-a-b)])
    return ans