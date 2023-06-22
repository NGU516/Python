import sys
N, M = map(int, input().split())

password = {}

for i in range(N):
    index, value = sys.stdin.readline().split()
    password[index] = value
    
for i in range(M):
    search = sys.stdin.readline().rstrip()
    if password[search]:
        print(password[search])

