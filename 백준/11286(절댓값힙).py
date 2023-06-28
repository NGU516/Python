import heapq
import sys
input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    temp = int(input())
    if temp == 0 and arr != []: 
        print(heapq.heappop(arr)[1])
    elif temp == 0 and arr == []: # 비어있을 경우
        print(0)
    else:
        heapq.heappush(arr, (abs(temp), temp))
