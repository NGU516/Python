import sys

while True:
    input = sys.stdin.readline().rstrip()
    if input == '.':
        break
    
    stack = []
    is_balanced = True

    for char in input:  # 괄호 균형 확인(stack)
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                is_balanced = False
                break
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                is_balanced = False
                break
            stack.pop()

    if stack != [] or is_balanced == False:
        print('no')
    else:
        print('yes')

# 스택 구현 왼쪽괄호 append 오른쪽 괄호 나오면 pop
