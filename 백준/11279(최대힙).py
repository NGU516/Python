import heapq
import sys

N = int(sys.stdin.readline().rstrip())

max_heap = []

# 0 출력, 나머지 입력
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    
    # 0이 아닐 때
    if x != 0:
        heapq.heappush(max_heap, (-x, x))

    # 배열이 비어있는 경우
    if not max_heap:
        print(0)
        
    # 출력
    elif max_heap and (x == 0):
        print(heapq.heappop(max_heap)[1])
