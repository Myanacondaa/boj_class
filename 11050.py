import sys
from math import factorial
input = sys.stdin.readline

N, K = map(int, input().split())

print(int(factorial(N)/(factorial(K)*factorial(N-K))))