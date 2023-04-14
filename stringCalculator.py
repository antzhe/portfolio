# Функция перевода строки в обратную польскую запись
def rpn(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = []
    output = []
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            output.append(" ")
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            output.append(" ")
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                output.append(stack.pop())
                output.append(" ")
            stack.append(char)
    while stack:
        output.append(" ")
        output.append(stack.pop())
    return ''.join(output)

math_str = input()
RPN = rpn(math_str)
result = []
for i in RPN.split():
    if i.isdigit():
        result.append(int(i))
    else:
        if i == '+':
            b = result.pop()
            a = result.pop()
            res = a + b
            result.append(res)
        elif i == '-':
            b = result.pop()
            a = result.pop()
            res = a - b
            result.append(res)
        elif i == '*':
            b = result.pop()
            a = result.pop()
            res = a * b
            result.append(res)
        elif i == '/':
            b = result.pop()
            a = result.pop()
            res = a / b
            result.append(res)
        elif i == '^':
            b = result.pop()
            a = result.pop()
            res = a**b
            result.append(res)
print(int(result[0]))