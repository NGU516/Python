n = int(input())
a = list(map(int, input().split()))

sorted_a = sorted(a)
swap_count = 0

# 각 원소의 인덱스를 저장하는 딕셔너리 생성
idx_dict = {}
for i, v in enumerate(a):
    idx_dict[v] = i

for i in range(n):
    if a[i] != sorted_a[i]:
        j = idx_dict[sorted_a[i]]
        a[i], a[j] = a[j], a[i]
        idx_dict[a[j]] = j
        swap_count += 1

print(swap_count)
