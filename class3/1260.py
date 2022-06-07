def dfs(v: int):
    visited1[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if not visited1[i] and graph[v][i] == 1:
            dfs(i)


def bfs(v: int):
    qu = [v]
    visited2[v] = True
    while qu:
        v = qu.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if not visited2[i] and graph[v][i] == 1:
                qu.append(i)
                visited2[i] = True


if __name__ == "__main__":
    n, m, v = map(int, input().split())
    graph = [[0]*(n+1) for _ in range(n+1)]
    visited1 = [False]*(n+1)        # dfs 방문 노드 리스트
    visited2 = [False]*(n+1)        # bfs 방문 노드 리스트
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1

    dfs(v)
    print()
    bfs(v)