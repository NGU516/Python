n = int(input())
#set() 중복 허용 x 배열 생성, 입력된 순서로 저장되지 않음
x = set(map(int, input().split()))
m = int(input())
y = map(int, input().split())

# for반복문에 in()포함여부 함수 y안에 x값의 존재여부 확인
for num in y:
    if num in x:
        print(1)
    else:
        print(0)

""" (시간초과)
n = int(input())
#list() 리스트에 저장
x = list(map(int, input().split()))
m = int(input())
y = list(map(int, input().split()))

# for반복문에 in()포함여부 함수 y안에 x값의 존재여부 확인
for num in y:
    if num in x:
        print(1)
    else:
        print(0)
"""