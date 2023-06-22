# n개의 문자열로 이루어진 집합 s
# 입력 m개의 문자열 중에 집합 s에 포함되는 것은?

# 문자열 집합 s (n = 개수)
set_s = []
# 입력값
set_m = []
# 포합되어 있는 문자열
count = 0

n, m = input().split()
n = int(n)
m = int(m)

# 입력받기
for i in range(n):
    set_s.append(input())
for i in range(m):
    set_m.append(input())

set_s = set(set_s)
# 집합안에 있는 값이 리스트에 있으면 카운트
for string in set_m:
    if string in set_s:
        count += 1
# 집합 s와 입력받은 집합 m 비교(m개만큼)
print(count)
