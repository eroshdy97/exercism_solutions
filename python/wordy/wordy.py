from operator import truediv


def answer(question):
    if question[-1] == '?':
        question = question[:-1]
    else:
        raise ValueError("syntax error")

    
    question:list = question.split()
    question.reverse()

    exp_num:bool = None
    exp_by:bool = None
    operands = []
    operators = []
    while question:
        word:str = question.pop()

        if word == "What":
            continue
        elif word == "is":
            exp_num = True
            continue
        elif word == "by" and exp_by:
            exp_num = True
            exp_by = False
            continue

        elif word.isdigit() and exp_num:
            operators.append(int(word))
            exp_num = False

        elif word[0] == "-" and word[1:].isdigit() and exp_num:
            operators.append(int(word))
            exp_num = False

        elif word == "plus" and not exp_num:
            exp_num = True
            operands.append("+")
        
        elif word == "minus" and not exp_num:
            exp_num = True
            operands.append("-")

        elif word == "multiplied" and not exp_num:
            exp_num = False
            exp_by = True
            operands.append("*")

        elif word == "divided" and not exp_num:
            exp_num = False
            exp_by = True
            operands.append("/")

        else: 
            # raise ValueError("unknown operation") 
            # raise ValueError("syntax error")
            if exp_num and operands and operators:
                raise ValueError("syntax error")
            if not exp_num and operands and operators:
                raise ValueError("syntax error")
            if not exp_num and operands and not operators:
                raise ValueError("syntax error")
            if not exp_num and not operands and operators and not word.isdigit():
                raise ValueError("unknown operation")
            if exp_num and not operands and not operators:
                raise ValueError("syntax error")
            if exp_num == None and exp_by == None:
                raise ValueError("unknown operation")
            raise ValueError("syntax error")

            

    operands.reverse()
    operators.reverse()
    if len(operators) == len(operands) + 1:
        res = operators.pop()
        while operands:
            op = operands.pop()
            if op == "+":
                res += operators.pop()
            if op == "-":
                res -= operators.pop()
            if op == "*":
                res *= operators.pop()
            if op == "/":
                res /= operators.pop()
        
    else:
        raise ValueError("syntax error")

    return res

