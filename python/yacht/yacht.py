# Score categories.
# Change the values as you see fit.


ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12

def score(dice, category):
    if category == ONES:
        return dice.count(1)

    elif category == TWOS:
        return 2 * dice.count(2)

    elif category == THREES:
        return 3 * dice.count(3)

    elif category == FOURS:
        return 4 * dice.count(4)

    elif category == FIVES:
        return 5 * dice.count(5)

    elif category == SIXES:
        return 6 * dice.count(6)

    elif category == FULL_HOUSE:
        num1 = [x for x in dice if dice.count(x) == 3]
        num2 = [x for x in dice if dice.count(x) == 2]
        if len(num1) >= 1 and len(num2) >= 1:
            return sum(dice)
        else:
            return 0

    elif category == FOUR_OF_A_KIND:
        num = [x for x in dice if dice.count(x) >= 4]
        if len(num) >= 1:
            return 4 * num[0]
        else:
            return 0

    elif category == LITTLE_STRAIGHT:
        if dice.count(1) and dice.count(2) and dice.count(3) and dice.count(4) and dice.count(5):
            return 30
        else:
            return 0
    
    elif category == BIG_STRAIGHT:
        if dice.count(6) and dice.count(2) and dice.count(3) and dice.count(4) and dice.count(5):
            return 30
        else:
            return 0

    elif category == CHOICE:
        return sum(dice)

    elif category == YACHT:
        if dice.count(dice[0]) == 5:
            return 50
        else:
            return 0

    else :
        return 0
    

