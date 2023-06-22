N = int(input())
list_N = input().split()

# 요소 int형으로 변환 -> 다시 list type 변환
list_N = map(int, list_N)
list_N = list(map(int, list_N))

# set()으로 중복제거 type = set -> 다시 list type 변환
list_N = set(list_N)
list_N = list(list_N)

# list 오름차순 처리
list_N.sort()
print(*list_N)
