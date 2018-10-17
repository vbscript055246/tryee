
def calPostfix(str):
    stack = list()
    for item in str.split():
        if item in "*/+-":
            temp = eval("{}{}{}".format(stack[-2], item, stack[-1]))
            stack.pop()
            stack.pop()
            stack.append(temp)
        else:
            stack.append(item)
    return stack[-1]


print(calPostfix("10 8 + 6 5 * -"))