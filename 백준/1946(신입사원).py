# 서류심사 성적 and 면접시험 성적 중
## 성적이 아니라 성적 순위
#### 적어도 하나가 다른 지원자보다 떨어지지 않는 자 선발
# 선발할 수 있는 최대 인원 수
# 동석차 존재 x

## 면접 따로 서류 성적 min()
## 서류 따로 면접 성적 min()
### 면접최소 성적인 사람 서류성적 순위 비교
### 서류최소 성적인 사람 면접성적 순위 비교
import sys 
# test case
t = int(sys.stdin.readline())

for i in range(t):
    # n개만큼 2차원 배열 입력
    list_n = []
    n = int(sys.stdin.readline())

    for i in range(n):
        list_n.append(list(map(int, sys.stdin.readline().split())))

    list_n.sort()
    a = list_n[0][1] # 면접 1등의 성적의 순위
    cnt = 0

    # 면접 1등보다 성적순위가 낮은 사람 cnt
    # i는 리스트인덱스를 뜻함 ex) i[1] -> list_n[1]
    for i in list_n:
        if i == list_n[0]:
            cnt += 1
        elif i[1] < a:
            cnt += 1
            a = i[1]
    # testcase 출력
    print(cnt)

"""
각 줄마다를 한 사람으로 인식
면접 성적순(사람 = index)
성적 성적순(사람 = index)
각 분야의 1등의 다른 성적을 기준으로 나누기
그 사이에서 반복문으로 값 비교
"""

