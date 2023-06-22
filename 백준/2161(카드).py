from collections import deque
N = int(input())
card = deque([i for i in range(1,N+1)])

while card:
    # 제일 위에 카드 버리기
    print(card.popleft(),end=' ')

    if card:
        # 그 다음 제일 위에 카드 제일 아래로
        card.append(card.popleft())
    else:
        break
