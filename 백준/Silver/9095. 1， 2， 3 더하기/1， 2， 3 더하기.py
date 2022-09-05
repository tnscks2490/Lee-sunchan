import sys

N = int(sys.stdin.readline())

dp = [0,1,2,4] + [0] * 8
for i in range(4,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(N):
    print(dp[int(sys.stdin.readline())])