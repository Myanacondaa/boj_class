from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    d = defaultdict(int)
    for _ in range(n):
        cloth, wear = map(str, input().split())
        if wear in d:
            d[wear] += 1
        else:
            d[wear] = 1

    # 경우의 수 = (상의 개수 + 1)*(하의 개수 +1) * ...  - 1
    case = 1
    for v in d.values():
        case *= (v+1)   # 개수 +1 (안입을 경우의 수 포함) 곱하기

    print(case-1)       # 모두 안입을 경우의 수인 1 빼기