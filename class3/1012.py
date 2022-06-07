# 섬의 개수와 같은 문제
import sys
sys.setrecursionlimit(10**6)
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())         # 가로, 세로, 배추 개수
    cabbage = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        cabbage[y][x] = 1


    def dfs(x, y):
        if x < 0 or y < 0 or x >= n or y >= m or cabbage[x][y] == 0:
            return

        cabbage[x][y] = 0

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)


    cnt = 0
    for i in range(n):
        for j in range(m):
            if cabbage[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)




