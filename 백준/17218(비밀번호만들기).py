# 최장 공통 부분수열(Longest Common Subsequence)
# AUTABBEHNSA
# BCUAMEFKAJNA
# 순서를 고려하기 때문에 set() 사용 x
import sys
a = list(map(str, sys.stdin.readline().strip()))
b = list(map(str, sys.stdin.readline().strip()))

# a, b로 이루어진 행렬구성
# 첫번째값은 편의상 0 -> 길이+1
LCS = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            # 두 문자가 일치하지 않는 경우, 
            # LCS[i][j]는 이전 LCS의 길이 중에서 최대값
            LCS[i][j] = max(LCS[i][j - 1], LCS[i - 1][j])

# LCS의 최대값을 찾아 역추적
i = len(a)
j = len(b)
lcs = []
while i > 0 and j > 0:
    if a[i - 1] == b[j - 1]:
        lcs.append(a[i - 1])
        i -= 1
        j -= 1
    else:
        if LCS[i][j - 1] > LCS[i - 1][j]:
            j -= 1
        else:
            i -= 1

# 결과 출력
print(''.join(reversed(lcs)))
