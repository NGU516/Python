import math # math.lcm(최소공배수)

T = int(input())
list_A = []
list_B = []
list_lcm = []
# A,B 리스트에 값 넣기
for i in range(T):
    A, B = input().split()
    list_A.append(A)
    list_B.append(B)
# 리스트내의 값 str -> int (class 'map -> class 'list')
list_A = map(int,list_A)
list_A = list(list_A)
list_B = map(int,list_B)
list_B = list(list_B)

for i in range(T):
    lcm = math.lcm(list_A[i], list_B[i])
    list_lcm.append(lcm)

for i in range(T):
    print(list_lcm[i])