# c:1 d:2 e:3 f:4 g:5 a:6 b:7 C:8
# ascending = 1~8순서대로, descending = 8~1 순서
# mixed = else

# 음계 숫자로 입력받기
scale = list(map(int, input().split()))
ascending_cnt = 0
descending_cnt = 0

for i in range(len(scale)-1):
    if scale[i+1] - scale[i] == 1:
        ascending_cnt += 1
    elif scale[i+1] - scale[i] == -1:
        descending_cnt += 1

if ascending_cnt == 7:
    print("ascending")
elif descending_cnt == 7:
    print("descending")
else:
    print("mixed")