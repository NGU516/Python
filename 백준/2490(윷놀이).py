# 배(0), 등(1)
# 도(0), 개(00), 걸(000), 윷(0000), 모(1111)
# A B C D E
import sys

while True:
    input = list(map(str, sys.stdin.readline().strip()))
    zero = input.count('0') # 배(0) 
    if zero == 1:
        print('A')
    elif zero == 2:
        print('B')
    elif zero == 3:
        print('C')
    elif zero == 4:
        print('D')
    elif zero == 0 and input.count('1') == 4:
        print('E')
    else:
        break



