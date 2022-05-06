import sys
import math as m
input = sys.stdin.readline

N,M = map(int, input().split())
print(m.gcd(N,M))
print(m.lcm(N,M))