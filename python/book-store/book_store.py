def claculate_fours(num_books):
    ans = 0
    book_price = 8
    discounts = [1, 0.95, 0.9, 0.8, 0.75]
    num_diff_books = len([i for i in num_books if i > 0])
    total_num_books = sum(num_books)

    num_fours = 0
    while total_num_books >= 8 and num_diff_books >= 4 :
        for i in range(4):
            num_books[i] -= 1
        num_books = sorted(num_books, reverse=True)
        num_fours += 1
        num_diff_books = len([i for i in num_books if i > 0])
        total_num_books = sum(num_books)
        print("modified book list :", num_books)
        print("num_diff_books = ", num_diff_books, " total_num_books = ", total_num_books)
    
    ans = round((claculate_fives(num_books) + num_fours * 4 * book_price * discounts[3])*100)
    return ans

def claculate_fives(num_books):
    ans = 0
    book_price = 8
    discounts = [1, 0.95, 0.9, 0.8, 0.75]

    while max(num_books) > 0:
        books = 0
        for i, count in enumerate(num_books):
            if count > 0:
                num_books[i] -= 1
                books += 1
        ans += books * book_price * discounts[books-1]
    return ans

def total(basket):
    num_books = [
    len([i for i in basket if i == 1]),
    len([i for i in basket if i == 2]),
    len([i for i in basket if i == 3]),
    len([i for i in basket if i == 4]),
    len([i for i in basket if i == 5])
    ]
    num_books = sorted(num_books, reverse=True)
    print("original book list :", num_books)

    ans = [claculate_fours(num_books)]

    num_books = [
    len([i for i in basket if i == 1]),
    len([i for i in basket if i == 2]),
    len([i for i in basket if i == 3]),
    len([i for i in basket if i == 4]),
    len([i for i in basket if i == 5])
    ]
    num_books = sorted(num_books, reverse=True)

    ans.append(claculate_fives(num_books)*100)

    return round(min(ans))