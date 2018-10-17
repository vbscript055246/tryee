str = input()
stack = list()
stable = {'*': 2, '/': 2, '%': 2, '+': 3, '-': 3, '(': 8}
itable = {'*': 2, '/': 2, '%': 2, '+': 3, '-': 3, '(': 0}
for char in str:
    if char in "+-*/(":
        if len(stack):
            if stable[stack[-1]] <= itable[char]:
                print(stack[-1], end="")
                stack.pop()
        stack.append(char)
    elif char == ')':
        while stack[-1] != '(':
            print(stack[-1], end="")    # A*(B+C)*D
            stack.pop()
        stack.pop()
    else:
        print(char, end="")

while len(stack):
    print(stack[-1], end="")
    stack.pop()
