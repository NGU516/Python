import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)
result = 0

while start <= end:
    # 현재 기준 나무
    mid = (start + end) // 2

    # 가져가는 나무의 길이
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid

    # 가져가는 나무가 M보다 크거나 같을 때
    if total >= M:
        result = mid
        # 기준치 올림
        start = mid + 1
    # 가져가는 나무가 M보다 작을 때    
    else:
        # 기준치 내림
        end = mid - 1

print(result)
