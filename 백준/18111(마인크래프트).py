import sys
N, M, B = map(int,input().split())
block = []

for _ in range(N):
    block.append([int(x) for x in sys.stdin.readline().split()])

min_time = int(1e9)
target_floor = 0

# 모든 층 검사
for i in range(257):

    # 작업 1 : 블록제거 후 인벤토리 보관 (2초)
    take_block = 0
    # 작업 2 : 블록설치 (1초)
    use_block = 0

    for x in range(N):
        for y in range(M):
            # 블록이 더 높을 경우(작업1)
            if block[x][y] > i:
                take_block += block[x][y] - i
            # 블록이 더 낮을 경우(작업2)
            else:
                use_block += i - block[x][y]

    # 사용한 블럭이 지닌 블록보다 많을 경우 다음 층 조사
    if use_block > take_block + B:
        continue

    # 작업을 통한 시간계산
    time = take_block * 2 + use_block

    # 조사한 시간이 더 작을 경우 최소시간과 해당 층 기억
    if time <= min_time:
        min_time = time
        target_floor = i
    
print(min_time,target_floor)