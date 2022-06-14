t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    tmp = True
    while x <= m*n:
        if x % n == y % n:
            print(x)
            tmp = False
            break
        x += m

    if tmp:
        print(-1)
