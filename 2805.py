import sys
input = sys.stdin.readline


def cutting_tree(h: int, t: list[int]) -> int:
    t.sort(reverse=True)
    cutter = 0
    tree_sum = -h
    for i in range(len(t)):
        tree_sum += t[i]
        result = tree_sum/(i+1)  # sum(t[:i+1])-h)/(i+1)
        if result > cutter:
            cutter = result
    return int(cutter)

if __name__ == "__main__":
    N, M = map(int, input().split())
    tree = list(map(int, input().split()))
    print(cutting_tree(M, tree))