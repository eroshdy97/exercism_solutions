def find(search_list, value):
    length = len(search_list)
    
    max_index = length - 1
    mid_index = int((max_index) / 2)

    if length == 0 or (length == 1 and value is not search_list[mid_index]):
        raise ValueError("value not in array")
    
    
    if value == search_list[mid_index]:
        return mid_index

    elif value > search_list[mid_index]:
        return find(search_list[mid_index + 1: ], value) + mid_index + 1

    elif value < search_list[mid_index]:
        return find(search_list[: mid_index], value)
