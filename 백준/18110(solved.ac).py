import sys
from collections import deque

def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

N = int(sys.stdin.readline())

# 절사평균 15%
average_cut = round2(N * 0.15)
difficulty = []

for _ in range(N):
    temp = int(sys.stdin.readline())
    difficulty.append(temp)

# 난이도 정리(정렬후 deque 저장)
difficulty.sort()
sort_difficulty = deque(difficulty)

# 앞 뒤 15%씩 제거
for _ in range(average_cut):
    if sort_difficulty:
        sort_difficulty.pop()
for _ in range(average_cut):
    if sort_difficulty:
        sort_difficulty.popleft()

if sort_difficulty:
    average_difficulty = round2(sum(sort_difficulty) / len(sort_difficulty))
else:
    average_difficulty = 0

print(average_difficulty)
