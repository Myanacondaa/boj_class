import sys
input = sys.stdin.readline

dp = [0]*102

t = int(input())
for _ in range(t):
    n = int(input())
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-3]+dp[i-2]

    print(dp[n-1])