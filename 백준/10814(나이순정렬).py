import sys
N = int(input())

user_temp = []
user = []

for i in range(N):
    user_temp = sys.stdin.readline().split()
    user.append(user_temp)
    user[i][0] = int(user[i][0])
    
user.sort(key = lambda x:x[0])

for i in range(N):
    print(" ".join(map(str, user[i])))
