import sys
input = sys.stdin.readline

N, S = map(int, input().split())
coins = []
min_limit = 0
cnt = 0
for _ in range(N):
    v, a = map(int, input().split())
    min_limit += v * a
    cnt += a
    coins.append(v)

if S < min_limit:
    print(-1)
else:
    rest = S - min_limit
    dp = [30000001] * (rest + 1) 
    dp[0] = 1
    for i in range(N-1, -1, -1):
        j = 0
        while j < rest+1 - coins[i]:
            if dp[j]:
                dp[j+coins[i]] = min(dp[j+coins[i]], dp[j] + 1)
            j += 1
    if dp[rest] != 30000001:
        print(dp[rest]-1 + cnt)
    else:
        print(-1)