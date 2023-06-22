n = int(input())

coordinate = []
for i in range(n):
    coordinate_in = list(map(int, input().split()))
    coordinate.append(coordinate_in)

coordinate.sort(key=lambda x:(x[1],x[0]))

for i in range(n):
    print(coordinate[i][0], coordinate[i][1])