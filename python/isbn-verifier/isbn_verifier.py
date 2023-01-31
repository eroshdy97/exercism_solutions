from asyncio.format_helpers import _format_callback_source


def is_valid(isbn):
    valid = '0123456789X-'

    if len(isbn) == 0 or [x for x in isbn if x not in valid]:
        return False
    
    # if isbn[-1] == 'X':
    #     isbn = isbn[:-1]
    #     isbn += '10'

    chars = '0123456789X'
    isbn = [x for x in isbn if x in chars]
    
    if isbn[-1] == 'X':
        isbn.pop()
        isbn.append('10')

    numbers = '0123456789'
    if len(isbn) != 10 or [x for x in isbn[:-1] if x not in numbers]:
        return False

    sum = 0
    for i in range(len(isbn)):
        sum += int(isbn[i]) * (10 - i)
    
    return sum % 11 == 0
