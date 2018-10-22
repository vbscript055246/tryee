import re
string1 = "10*(45*21+76)/(87*9)"
string2 = "34*12/(56/4)+56*34*17"
string3 = "3*(6+2)*5"


def get_prefix(string):
    return str(string[1] + string[0] + string[2])


def prefix(string):
    stack = re.findall("[[0-9]{1,}|[*/+\-\(\)]]*", string)
    while 1:
        try:
            n = stack.index('(')
            temp = 0
            m = -1
            for index, item in enumerate(stack[n+1:]):
                if item == '(':
                    temp += 1
                elif temp and item == ')':
                    temp -= 1
                elif item == ')':
                    m = n + index

            s = prefix(''.join(stack[n+1:m+1]))
            del stack[n:m+2]
            stack.insert(n, s)
        except:
            break

    while len(stack) > 1:
        for index, item in enumerate(stack):
            if item == '*' or item == '/':
                s = get_prefix(stack[index-1:index+2])
                del stack[index-1:index+2]
                stack.insert(index-1, s)

        for index, item in enumerate(stack):
            if item == '+' or item == '-':
                s = get_prefix(stack[index-1:index+2])
                del stack[index-1:index+2]
                stack.insert(index-1, s)

    return ''.join(stack)


def recurse_calprefix(string):
    if len(string) == 1:
        return int(string)
    if string[1].isdigit():
        return eval(str(recurse_calprefix(string[2:])) + string[0] + string[1])
    else:
        return eval(str(recurse_calprefix(string[1:-1])) + string[0] + string[-1])


print(prefix(string3))
print(recurse_calprefix(prefix(string3)))

