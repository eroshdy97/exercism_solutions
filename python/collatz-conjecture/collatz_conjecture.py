def steps(number):
    if(number < 1):
        raise ValueError("Only positive integers are allowed")
    step = 0
    while(True):
        if(number == 1):
            break
        elif (number % 2 == 0):
            number /= 2
            step += 1
            continue
        else:
            number = number * 3 + 1
            step += 1
            continue
    return step

