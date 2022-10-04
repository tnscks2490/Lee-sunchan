import sys
N = int(sys.stdin.readline())

dp = [0] * ((N//5) + 1)

for i in range(len(dp)):
    if (N - (i*5)) % 2 == 0:
        dp[i] = i + (N - (i*5)) // 2
    else:
        dp[i] = 100000

if min(dp) == 100000:
    print(-1)
else:
    print(min(dp))