import sys
L = int(input())
string_list = list(map(str, sys.stdin.readline()))

alpha_num = []
hash = 0

# ord() 유니코드 문자에 대응되는 정수반환
for i in range(L):
    alpha_num.append(ord(string_list[i]) - 96)

for i in range(L):
    hash += alpha_num[i] * 31 ** i

print(hash % 1234567891)
    
# 31**i
# a=1, b=2