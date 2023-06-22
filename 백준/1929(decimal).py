import math
n = list(map(int, input().split()))

# 소수 판별 함수
def prime_number(x):
    # 1은 제외
    if x == 1:
        return False
    # 2부터 x의 제곱근(정수형태)까지 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            # 나누어떨어지면 소수아님
            return False
    return True

for i in range(n[0], n[1]+1):
    if prime_number(i) == True:
        print(i)

