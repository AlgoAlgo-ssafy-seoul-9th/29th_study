import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))

tmp = 0
rest = [0] * (N+1)
dp = [0]*(N+1)
for i in range(1, N+1):
    rest[i] = nums[i] % M     # num을 M으로 나눈 나머지 리스트

for i in range(1, N+1):
    tmp = (tmp + rest[i]) % M   # 현재 값에 더하고 M으로 나눈 값
    if tmp == 0:
        dp[i] = dp[i-1]+1
    else:
        dp[i] = dp[i-1]

ans = 0
for i in range(N, 0, -1):
    ans += (dp[N] - dp[i])

print(ans)