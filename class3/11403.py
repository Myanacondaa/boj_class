n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):      # 플로이드 워셜
    for a in range(n):
        for b in range(n):
            # a > b 경로가 있거나 a > k > b 경로가 있으면 1
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                graph[a][b] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()
