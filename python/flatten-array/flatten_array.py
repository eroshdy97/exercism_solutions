def flatten(iterable): # [5, [1, 2, 3], [[100]]]
    output = []
    if hasattr(iterable, '__iter__'):
        for item in iterable:
            if item == None:
                continue
            output += list(flatten(item))
        return output
    elif iterable == None:
        return []
    else:
        return [iterable]



