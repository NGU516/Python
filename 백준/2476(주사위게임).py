# a,b,c 주사위 3개로 상금 (n명)
# if a == b == c 10,000 + (눈 값*1,000)
# elif a == b or b == c or a == c 1,000 + (눈 값*100)
# else a,b,c 중 가장 큰 값 * 100
# 가장 많은 상금을 받은 사람의 상금 출력

N = int(input()) # 참여자 수

list_n = []
for i in range(N):
    a, b, c = map(int, input().split())
    money = 0 # 상금
    if a == b == c:
        money = 10000 + (a * 1000)
    elif a == b or b == c or a == c:
        money = 1000 + (max(a, b, c) * 100)
    elif a > b and a > c:
        money = a * 100
    elif b > a and b > c:
        money = b * 100
    elif c > a and c > a:
        money = c * 100
    list_n.append(money) # list_n에 계산값 저장 list_n.append(상금)

print(max(list_n))