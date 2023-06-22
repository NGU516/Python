N = int(input())
stair = []
score = []

for i in range(N):
    stair.append(int(input()))

if N == 1: # 계단의 개수가 1인경우
    print(stair[0])
    exit(0)

if N == 2: # 계단의 개수가 2인경우
    print(stair[0] + stair[1])
    exit(0)

score.append(stair[0]) # score[0]
score.append(stair[0] + stair[1]) # score[1]
score.append(max(stair[1] + stair[2], stair[0] + stair[2])) # score[2] 한칸, 두칸 중 최대값

for i in range(3, N):
    score.append(max(score[i - 3] +  stair[i - 1] + stair[i],
                score[i - 2] + stair[i]))
    
print(score[-1])
print(score)