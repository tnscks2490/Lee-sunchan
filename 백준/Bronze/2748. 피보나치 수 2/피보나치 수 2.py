import sys

N = int(sys.stdin.readline())
dp = [0,1,1,2] + [0] * (N-1)
for i in range(4,N+1):
    dp[i] =  dp[i-1] + dp[i-2]
print(dp[N])