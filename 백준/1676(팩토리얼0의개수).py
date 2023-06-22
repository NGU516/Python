import math

n = int(input())
nf = str(math.factorial(n))
list_N = []

for i in reversed(range(len(nf))):
    list_N.append(nf[i])

i = 0
cnt = 0

while True:
    if i == len(list_N):
        break
    if list_N[i] == "0":
        cnt += 1
    else:
        break
    i += 1
        
print(cnt)
