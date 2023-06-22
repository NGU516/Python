import sys

toy_str = []
max_len = 0

# 글자 입력받기(2차원 배열)
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break

    toy_str.append(list(line))
    max_len = max(max_len, len(line))

# 짧은 행에 맞춰서 세로로 읽기
for i in range(max_len):
    for j in range(len(toy_str)):
        if i < len(toy_str[j]):
            print(toy_str[j][i], end='')


"""
[0][0]
[1][0]
[2][0]
[3][0]
[4][0]
[5][0]
[0][1]
[1][1]
[2][1]
"""
