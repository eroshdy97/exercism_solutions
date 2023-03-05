def transpose(lines):
    result = []
    for line_index, line in enumerate(lines.splitlines()):
        for char_index, char in enumerate(line):
            while len(result) <= char_index:
                result.append([])

            while len(result[char_index]) < line_index:
                result[char_index].append(' ')
                
            result[char_index].append(char)

    return '\n'.join(''.join(row) for row in result)