import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(heap, a)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)