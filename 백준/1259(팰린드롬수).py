# 121, 12421 뒤에서부터 읽어도 같은 수 = 팰린드롬수

while True:
    n = input()
    # 팰린드롬 수 판별
    if n == '0':
        break
    elif n == n[::-1]:
        print("yes")
    else:
        print("no")