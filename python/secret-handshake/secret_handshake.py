def commands(binary_str):
    code = ['wink', 'double blink', 'close your eyes', 'jump']
    output = []
    for index, num in enumerate(binary_str[1:]):
        if num == '1':
            output.insert(0, code[3 - (index)])
    
    if(binary_str[0]) == '1':
        output.reverse()

    return output