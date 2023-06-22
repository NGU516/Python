# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.
import sys

global S
S = set()

N = int(input())
for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    operation = command[0]
    if operation == 'add':
        S.add(int(command[1]))
    elif operation == 'remove':
        S.discard(int(command[1]))
    elif operation == 'check':
        if int(command[1]) in S:
            print(1)
        else:
            print(0)
    elif operation == 'toggle':
        x = int(command[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif operation == 'all':
        S = set(range(1, 21))
    elif operation == 'empty':
        S.clear()


    