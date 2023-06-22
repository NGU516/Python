# n장의 카드
# 1~n 위에부터 1~n
# 맨 위 버리고 다음장은 맨 뒤로 반복
# 마직막의 남는 카드 번호는?

from collections import deque

def josephus(n):
    # 1~n번 카드
    queue = deque(range(1, n+1))
    # 큐의 길이가 1보다 클 때까지1
    while len(queue) > 1:
        # 첫번째 지우고 그 다음 뒤로 넘기고 반복
        for i in range(n-1):
            queue.popleft()
            queue.append(queue.popleft())
    return queue[0]

n = int(input())
print(josephus(n))




""" 시간초과
# n장의 카드
n = int(input())

# 1번부터 n번 카드
list_n = [i for i in range(1, n+1, 1)]

# 1장 남을 때까지 반복
while len(list_n) > 1:
    del list_n[0]
    list_n.append(list_n.pop(0))

print(list_n[0])
"""

