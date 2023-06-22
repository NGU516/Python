# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
from collections import deque
from sys import*
queue = deque()
n = int(input()) # 명령의 수

for i in range(n):
    arr = stdin.readline().split() # input()으로 받으면 시간초과
    if "push" in arr:
        queue.append(arr[1])
    elif "pop" in arr:
        if len(queue) == 0:
            print(-1)
        # 큐의 길이 1일 때는 삭제 후 -1 출력
        elif len(queue) == 1:
            print(queue.popleft())
        # 큐의 길이 2이상일 때
        else:
            print(queue.popleft())
    elif "size" in arr:
        print(len(queue))
    elif "empty" in arr:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif "front" in arr:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif "back" in arr:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])