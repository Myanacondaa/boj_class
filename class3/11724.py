import sys
sys.setrecursionlimit(10**4)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)


def dfs(v: int):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


cnt = 0

for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        cnt += 1

print(cnt)