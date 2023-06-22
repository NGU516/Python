K, N = map(int, input().split())

length = []

for i in range(K):
    length.append(int(input()))

if N == 1:
    print(max(length))
    exit()
    
start = 1
end = max(length)

result = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in length:
        # 주어진 랜선으로 만드는 랜선 개수
        count += i // mid
    
    if count >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
