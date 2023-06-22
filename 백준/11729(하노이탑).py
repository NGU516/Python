import sys

def hanoi(n, start = 1 , mid = 2, end = 3):
    if n == 1:
        print(start, end)
        return
    
    hanoi(n-1, start, end, mid)
    print(start, end)
    hanoi(n-1, mid, start, end)

N = int(input())
print((2**N)-1)
hanoi(N)
