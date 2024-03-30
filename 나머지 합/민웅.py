# 1, 2차시도
# 10986_나머지합_the remainder sum
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

n_lst = list(map(int, input().split()))

cnt = 0

prefix = [0]
rest_dict = {0: 1}
for i in range(N):
    tmp = (prefix[-1] + n_lst[i])%M
    if tmp in rest_dict.keys():
        cnt += rest_dict[tmp]
        rest_dict[tmp] += 1
    else:
        rest_dict[tmp] = 1
    prefix.append(tmp)

# (1차시도에 이 부분까지 포함)
# for i in range(N+1):
#     rest_dict[prefix[i]] -= 1
#     cnt += rest_dict[prefix[i]]

print(cnt)

'''
# 3차시도
# 10986_나머지합_the remainder sum
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

n_lst = list(map(int, input().split()))

cnt = 0
prefix = [0]
rest_dict = {0: 1}

for i in range(N):
    tmp = (prefix[-1] + n_lst[i]) % M
    cnt += rest_dict.get(tmp, 0)
    rest_dict[tmp] = rest_dict.get(tmp, 0) + 1
    prefix.append(tmp)

print(cnt)
'''