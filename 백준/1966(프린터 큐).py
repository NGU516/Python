from collections import deque

T = int(input())

for i in range(T):
    # 문서 개수, 궁금한 문서(위치)
    N, M = map(int, input().split())

    # 문서의 중요도 입력
    priorities = list(map(int, input().split()))
    
    # 문서 중요도 포함 큐 생성
    file = deque([(i, p) for i, p in enumerate(priorities)])

    # 카운트
    count = 0

    while True:
        # 중요도가 더 큰게 있는지 확인
        if any(file[0][1] < priorities for _, priorities in file):
            # 큐의 가장 뒤로 배치
            file.rotate(-1)

        else:
            document = file.popleft()
            count += 1
            if document[0] == M:
                break

    print(count)
