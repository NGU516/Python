import sys
import bisect
input = sys.stdin.readline

n = int(input())
list_n = sorted(list(map(int,input().split())))
m = int(input())
list_m = list(map(int,input().split()))

N_count = {}
for card in list_n:
    if card in N_count:
        N_count[card] += 1
    else:
        N_count[card] = 1

answer = []

for num in list_m:
    index = bisect.bisect_left(list_n, num)
    if index < n and list_n[index] == num:
        answer.append(N_count.get(num, 0))
    else:
        answer.append(0)

print(*answer)