N = int(input())
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(N):
    temp = int(input())
    if temp < 4:
        print(dp[temp])
    else:
        for i in range(4,temp+1):
            dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
        print(dp[temp])


# N = int(input())
# for _ in range(N):
#     a = int(input())
#     if a == 1:
#         print(2)
#     elif a == 2:
#         print(4)
#     elif a == 3:
#         print(7)
#     elif a == 4:
#         print(13)
#     elif a == 5:
#         print(24)
#     elif a == 6:
#         print(44)
#     elif a == 7:
#         print(81)
#     elif a == 8:
#         print(149)
#     elif a == 9:
#         print(274)
#     elif a == 10:
#         print(504)
#     elif a == 1:
#         print(927)




