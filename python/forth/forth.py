class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message

"""
 raising a StackUnderflowError
 raise StackUnderflowError("Insufficient number of items in stack")
 an example when division by zero is attempted.
 raise ZeroDivisionError("divide by zero")
 an example when the operation is undefined.
 raise ValueError("undefined operation") 
"""

def evaluate(input_data :list):
    stack = []
    user_defined = dict()

    inputs = [x.lower().split() for x in input_data]
    for line in inputs:
        if len(line) > 0 and line[0] != ":":
            for i, word in enumerate(line):
                if word in user_defined:
                    words = user_defined[word].split()
                    line[i] = words.pop()
                    while words:
                        line.insert(i, words.pop())
        print("line :", line)

        for input in line:
            if input.isnumeric():
                stack.append(int(input))
            elif input[0] == "-" and len(input) > 1:
                stack.append(int(input[1:]) * -1)

            elif input == "+":
                if not len(stack) == 2:
                     raise StackUnderflowError("Insufficient number of items in stack")
                temp = stack[0] + stack[1]
                stack.clear()
                stack.append(temp)

            elif input == "-":
                if not len(stack) == 2:
                     raise StackUnderflowError("Insufficient number of items in stack")
                temp = stack[0] - stack[1]
                stack.clear()
                stack.append(temp)

            elif input == "*":
                if not len(stack) == 2:
                     raise StackUnderflowError("Insufficient number of items in stack")
                temp = stack[0] * stack[1]
                stack.clear()
                stack.append(temp)

            elif input == "/":
                if not len(stack) == 2:
                     raise StackUnderflowError("Insufficient number of items in stack")
                if stack[1] == 0:
                    raise ZeroDivisionError("divide by zero")
                temp = stack[0] // stack[1]
                stack.clear()
                stack.append(temp)

            elif input.lower() == "dup":
                if not len(stack) > 0:
                     raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-1])

            elif input.lower() == "drop":
                if not len(stack) > 0:
                     raise StackUnderflowError("Insufficient number of items in stack")
                stack.pop()

            elif input.lower() == "swap":
                if not len(stack) > 1:
                     raise StackUnderflowError("Insufficient number of items in stack")
                temp = stack.pop()
                temp2 = stack.pop()
                stack.append(temp)
                stack.append(temp2)

            elif input.lower() == "over":
                if not len(stack) > 1:
                     raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-2])

            elif input == ":": # handel this line
                name = line[1]
                if name.isnumeric() or name[0] == "-":
                    raise ValueError("illegal operation")
                definition = line[2:-1]
                for i, x in enumerate(definition):
                    if x in user_defined:
                        definition[i] = user_defined[x]
                definition = " ".join(definition)
                while definition in user_defined:
                    definition = user_defined[definition]
                user_defined[name] = definition
                break

            else:
                raise ValueError("undefined operation")









    return stack
