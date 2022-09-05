import sys

N = int(sys.stdin.readline())
dp = [0,1,2,3] + [0] * (N-1)
for i in range(4,N+1):
    dp[i] =  (dp[i-1] + dp[i-2])%10007
print(dp[N])