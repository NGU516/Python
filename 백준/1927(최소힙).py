import heapq
import sys

N = int(sys.stdin.readline().rstrip())

min_heap = []

# 0 출력, 나머지 입력
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    
    # 0이 아닐 때
    if x != 0:
        heapq.heappush(min_heap, x)

    # 배열이 비어있는 경우
    if not min_heap:
        print(0)
        
    # 출력
    elif min_heap and (x == 0):
        print(heapq.heappop(min_heap))
