def value(colors):
    all_colors = ['black', 'brown', 'red', 'orange', 'yellow',
    'green', 'blue', 'violet', 'grey', 'white']

    output = ''
    for color in colors[:2]:
        if color in all_colors:
            output += str(all_colors.index(color))

    return int(output)
