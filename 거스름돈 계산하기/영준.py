N, S = map(int, input().split())
coin = [0] * N
coin_cnt = [0] * N
base = 0            # 최소 개수 합계금액
base_cnt = 0
for i in range(N):
    coin[i], coin_cnt[i] = map(int, input().split())
    base += coin[i]*coin_cnt[i]
    base_cnt += coin_cnt[i]
M = S-base
DP = [1000000]*(M+1) # 남은 금액을 DP로 
DP[0] = 0
for i in range(N):
    for j in range(1, M+1):   # i동전까지 고려해 j원 만들기
        if j>=coin[i]:      # 남은 거스름이 액면가 이상이면
            DP[j] = min(DP[j], DP[j-coin[i]]+1)

if DP[M]==1000000:
    print(-1)
else:
    print(base_cnt+DP[M])
