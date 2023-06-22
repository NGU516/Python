# 1 ~ n명  k번째 사람 제거
# 남은사람끼리 다시 원 구성
# n명이 제거될 때 까지
# 제거되는 순서 (n,k)요세푸스 순열
N, K = map(int, input().split())

list_N = list(range(1, N+1))
# 제거된 순서 list
list_per = []
index = 0
 
for i in range(N):
    index = (index + K - 1) % len(list_N)
    # 제거할 index list_per에 추가
    list_per.append(list_N.pop(index))

# .join 문자열합치기
print('<' + ', '.join(map(str, list_per)) + '>')