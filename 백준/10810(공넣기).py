N, M = map(int, input().split())
# N번 바구니
list_n = [0 for _ in range(N)]

# i,j,k i번~j번 바구니까지 k번 공을 넣음
# list.insert(바구니, 공 번호)
for i in range(M):
    I, J, K = map(int, input().split())
    for I in range(I, J+1):
        list_n[I-1] = K
        
print(*list_n)

