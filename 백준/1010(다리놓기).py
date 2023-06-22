import math
import sys

T = int(input())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(math.comb(M,N))

