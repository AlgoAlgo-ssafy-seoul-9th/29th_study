'''
5 3
1  2  3  1  2

i  j
i    ij
   i     j
i     i  i  j
'''


N, M = map(int, input().split())
arr = list(map(int, input().split()))
check = [0] * (N+1)     # i로 사용된 위치

total = 0
for i in range(N):
    tmp = 0
    cnt = 0
    if check[i]==0:     # i로 확정된 적이 없으면
        for j in range(i, N):
            tmp += arr[j]
            if tmp%M==0:
                cnt += 1
                check[j+1] = 1
                total += cnt

print(total)
