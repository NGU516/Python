# R B Y G 별로 1~9 (9*4=36)36장 중 5장 뽑기
cards = []
colors = [0 for _ in range(4)] # 0:R, 1:B, 2:Y, 3:G
numbers = [0 for _ in range(10)]

#색깔 숫자 담기 card[0] = 색깔 card[1] = 숫자
for i in range(5):
    card = list(input().split())
    cards.append(card)
    if card[0] == 'R':
        colors[0] += 1
    elif card[0] == 'B':
        colors[1] += 1
    elif card[0] == 'Y':
        colors[2] += 1
    else:
        colors[3] += 1
    numbers[int(card[1])] += 1

# 숫자 모두 연속
def check_number_serial(numbers):
    for i in range(6):
        if numbers[i] == 1 and numbers[i+1] == 1 and numbers[i+2] == 1 and numbers[i+3] == 1 and numbers[i+4] == 1:
            return True
    return False
# 1 색이 모두 같을 때
if check_number_serial(numbers):
    if 5 in colors:
        for i in range(9, 0, -1):
            if numbers[i] == 1:
                score = i + 900
                break
# 2 아닐 때
    else:
        for i in range(9, 0, -1):
            if numbers[i] == 1:
                score = i + 500
                break
elif not check_number_serial(numbers) and 5 in colors:
    for i in range(9, 0, -1):
        if numbers[i] == 1:
            score = i + 600
            break
# 4장이 같을 경우
elif 4 in numbers:
    score = numbers.index(4) + 800
# 3장이 같을 경우
elif 3 in numbers:
    if 2 in numbers:
        # 나머지 2장도 같을 경우 .index = 값이 3인 요소를 변수에 할당
        score = numbers.index(3) * 10 + numbers.index(2) + 700
    else:
        score = numbers.index(3) + 400
# 2장만 같을 경우
elif 2 in numbers:
    # 1 2.2.1 일 경우
    if numbers.count(2) == 2:
        idx = []
        for i in range(9, 0, -1):
            if numbers[i] == 2:
                idx.append(i)
        score = idx[0] * 10 + idx[1] + 300
    # 2 2장만 같을 경우
    else:
        for i in range(9, 0, -1):
            if numbers[i] == 2:
                score = i + 200
                break
else:
    for i in range(9, 0, -1):
        if numbers[i] == 1:
            score = i + 100
            break

print(score)


