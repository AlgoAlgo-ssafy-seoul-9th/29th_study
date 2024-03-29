import sys
input = sys.stdin.readline

N, S = map(int, input().split())

subsum = 0
cnt = 0
coins = []
for _ in range(N):
    v, a = map(int, input().split())
    subsum += v*a
    cnt += a
    coins.append(v)
coins.sort()
subsum = S - subsum
dp = [float('inf')]*(subsum+1)
dp[0] = 0
for i in range(1, N+1):
    for j in range(coins[i-1], subsum+1):
        dp[j] = min(dp[j-coins[i-1]] + 1, dp[j])

if dp[-1] != float('inf'):
    print(dp[-1]+cnt)
else:
    print(-1)