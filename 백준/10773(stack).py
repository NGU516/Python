n = int(input())
stack = []
sum = 0

for i in range(n):
    stack.append(int(input()))
    if stack[-1] == 0:
        stack.pop()
        stack.pop()

for i in stack:
    sum += i
    
print(sum)