def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    res = []
    for list in lists:
        for item in list:
            res.append(item)
    return res

def filter(function, list):
    res = []
    for item in list:
        if function(item):
            res.append(item)
    return res


def length(list):
    res = 0
    for item in list:
        res += 1
    return res


def map(function, list):
    res = []
    for item in list:
        res.append(function(item))
    return res


def foldl(function, list, initial):
    res = initial
    for item in list:
        res = function(res, item)
    return res


def foldr(function, list, initial):
    list.reverse()
    res = initial
    for item in list:
        res = function(item, res)
    return res


def reverse(list):
    list.reverse()
    return list
