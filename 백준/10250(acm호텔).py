T = int(input())

for _ in range(T):
    # 층 수, 방 수, 몇 번째 손님
    H, W, N = map(int, input().split())

    # 층번호 구하기(세로)
    count_H = N % H
    if count_H == 0:
        count_H = H

    # 방번호 구하기(가로)
    count_W = (N - 1) // H + 1
    
    # 출력
    room_number = count_H * 100 + count_W
    print(room_number)
