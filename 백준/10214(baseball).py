# 회차별 양 팀 획득 점수 data 처리
T = int(input())

for i in range(T):  
    Y, K = 0, 0
    for _ in range(9):
        del_Y, del_K = map(int,input().split())
        Y += del_Y
        K += del_K
    if Y > K:
        print("Yonsei")
    elif Y < K:
        print("Korea")
    else:
        print("Draw")
