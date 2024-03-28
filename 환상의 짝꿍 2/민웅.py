import sys
input = sys.stdin.readline

N, K = map(int, input().split())

n_lst = list(map(int, input().split()))

i, j = 0, N-1
n_lst.sort()
ans = "No"
while i < j:
    tmp = n_lst[i] + n_lst[j]
    if tmp == K:
        ans = "Yes"
        break
    if tmp > K:
        j -= 1
    else:
        i += 1

print(ans)