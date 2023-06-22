# stack 구현 함수
import sys
def is_VPS(list_VPS):
    stack_VPS = []
    for i in list_VPS:
        if i == "(":
            stack_VPS.append("(")
        elif stack_VPS and stack_VPS[-1] == "(":
            stack_VPS.pop()
        else:
            return "NO"
    if stack_VPS:
        return "NO"
    else:
        return "YES"

T = int(input())
for i in range(T):
    list_VPS = list(map(str, sys.stdin.readline()))
    # 개행문자 제거(sys.stdin.readline)
    list_VPS.pop()

    # 길이가 홀수이면 Not VPS
    if len(list_VPS) % 2 == 1:
        print("NO")
    else:
        print(is_VPS(list_VPS))