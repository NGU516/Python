n = int(input())

coordinate = []
for i in range(n):
    coordinate_in = list(map(int, input().split()))
    coordinate.append(coordinate_in)

coordinate.sort(key=lambda x:(x[0], x[1]))

for i in range(n):
    print(coordinate[i][0], coordinate[i][1])

# if x1 == x2 , y1 > y2
# (x1,y1)
# (x2,y2)
