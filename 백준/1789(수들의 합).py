# 자연수의 합 n(n+1)/2
S = int(input())

left, right = 1, S # 최대값은 1~S안에 존재
answer = 0

while left <= right:
    mid = (left + right) // 2 # 중간값에서 부터 이분탐색 시작
    if(mid * (mid + 1) / 2) <= S: # mid개의 자연수를 더한 값이 S보다 작으면 더 작은 값에서 이분탐색
        answer = mid
        left = mid + 1
    else:
        #print(f"mid:{mid}\nleft:{left}\nright:{right}\n") 
        right = mid - 1 # 더 작은 값에서 이분탐색
print(answer)