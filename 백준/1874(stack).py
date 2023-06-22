# push +
# pop -
n = int(input())
numarr = []
stack = []
output = []

for i in range(n):
    numarr.append(int(input()))

for i in range(1, n + 1):
    stack.append(i)
    output.append('+')

    while stack != [] and stack[-1] == numarr[0]:
        stack.pop()
        numarr.pop(0)
        output.append('-')
    
if numarr == []:
    for i in output:
        print(i)
elif numarr != []:
    print('NO')