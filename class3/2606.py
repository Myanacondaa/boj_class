from collections import defaultdict
n = int(input())        # 1이상 100 이하
m = int(input())        # 네트워크 상 직접 연결되어 있는 컴퓨터 수
graph = [[] for _ in range(n+1)]        # 0번째 인덱스는 사용하지 않음
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0]*(n+1)

def dfs(v:int):
    global cnt
    visited[v] = 1
    for w in graph[v]:
        if visited[w] == 0:
            dfs(w)
            cnt += 1

dfs(1)
print(cnt)
