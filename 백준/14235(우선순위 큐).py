from queue import PriorityQueue
import sys

N = int(input())

gift = PriorityQueue()

for _ in range(N):
    # 현재 방문지 == 0(아이들), == else 거점지 
    visit = list(map(int, sys.stdin.readline().split()))

    # 아이들을 만났을 때
    if visit[0] == 0:
        # 선물을 가지고 있을 때
        if not gift.empty():
            # -는 내림차순으로 출력하기 위함
            print(-gift.get())
        else:
            print(-1)
    # 거점지 방문
    else:
        for i,v in enumerate(visit):
            if i == 0:
                continue
            # 내림차순으로 반환
            gift.put(-v, v)
