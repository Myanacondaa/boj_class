import sys
input = sys.stdin.readline

cnt_minus_1 = 0
cnt_0 = 0
cnt_1 = 0

def sol(x:int, y:int, n:int):
    global cnt_minus_1, cnt_0, cnt_1

    check = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper[i][j]:
                check = -10
                break

    if check == -10:
        n //= 3
        sol(x, y, n)
        sol(x, y+n, n)
        sol(x, y+2*n, n)
        sol(x+n, y, n)
        sol(x+n, y+n, n)
        sol(x+n, y+2*n, n)
        sol(x+2*n, y, n)
        sol(x+2*n, y+n, n)
        sol(x+2*n, y+2*n,n)

    elif check == 0:        # 종이가 모두 0이면
        cnt_0 += 1
        return

    elif check == 1:       # 종이가 모두 1이면
        cnt_1 += 1
        return

    else:     # 종이가 모두 -1이면
        cnt_minus_1 += 1
        return


if __name__ == "__main__":
    n = int(input())
    paper = []
    for _ in range(n):
        paper.append(list(map(int, input().split())))
    sol(0, 0, n)

    print(cnt_minus_1)
    print(cnt_0)
    print(cnt_1)