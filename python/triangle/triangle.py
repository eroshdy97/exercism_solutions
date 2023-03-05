
def isValid(sides):
    if sides[0]+sides[1] >= sides[2] and sides[1]+sides[2] >= sides[0] and sides[2]+sides[0] >= sides[1]:
        return True
    else:
        return False


def equilateral(sides):
    if sides[0] == 0 or not isValid(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if not isValid(sides):
        return False
    return sides.count(sides[0]) >= 2 or sides.count(sides[1]) >= 2 


def scalene(sides):
    if not isValid(sides):
        return False
    return sides[0] != sides[1] != sides[2] != sides[0]
