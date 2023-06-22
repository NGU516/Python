n = int(input())  # 컴퓨터 수
m = int(input())  # 연결된 컴퓨터 쌍의 수

graph = [[] for _ in range(n+1)]  # 그래프 생성(2차원리스트)
visited = [False]*(n+1)  # 방문 여부 체크 리스트(각 요소 초기화)

# 그래프 생성
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

# DFS 함수 구현
def dfs(v):
    visited[v] = True  # 현재 노드 방문 처리
    for i in graph[v]:  # 현재 노드와 연결된 다른 노드들을 방문
        if not visited[i]:
            dfs(i)

dfs(1)  # 1번 컴퓨터부터 시작

# 감염된 컴퓨터 수 출력
print(visited.count(True)-1)  # 1번 컴퓨터 제외
