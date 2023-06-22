# 1 = 666, 2 = 1666, 3 = 2666
N = int(input())
list_num = []

for i in range(6666667):
    if '666' in str(i):
        list_num.append(i)
    elif '6666' in str(i):
        list_num.append(i)
    elif '66666' in str(i):
        list_num.append(i)
    elif '666666' in str(i):
        list_num.append(i)
list_num.sort()
print(list_num[N-1])

"""(최적화)
N = int(input())

num = 666
count = 0

while True:
    if '666' in str(num):
        count += 1
        if count == N:
            print(num)
            break
    num += 1

"""