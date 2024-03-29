# 29th_study
알고리즘 스터디 29주차

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [나머지 합](https://www.acmicpc.net/problem/10986)

### [민웅](/나머지%20합/민웅.py)

```py

```

### [상미](/나머지%20합/상미.py)

```py

```

### [성구](/나머지%20합/성구.py)

```py
# 10986 나머지 합
import sys
from collections import defaultdict
input = sys.stdin.readline

# 계획
'''
1. 구간 합 리스트 만들기
2. 구간 합 리스트의 각 인덱스를 M의 나머지로 저장하기
3. 각 나머지의 개수 중 2개를 선택하는 경우의 수 계산
    3-1. 나머지가 0 이상인 사항에서 대해
    구간합은 arr[j] - arr[i]로 구하며, 이는 나머지일때와 같은 결과를 갖음
    따라서, 나머지가 같은 구간끼리 빼면 나눠 떨어짐
    3-2. 그렇다면 같은 나머지에 대해서만 생각하면 됨
    3-3. 그 중 두 개가 만나면 나눠 떨어짐 -> nC2 계산
    3-3. 나머지가 0일 때는 그 자체로 개수로 인정됨
4. 나머지가 0인 구간 합과 더해서 출력
'''


def main():
    # 입력
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # settings
    remain = defaultdict(int)
    
    # 나머지의 개수 세기(구간합 구하기 + 나머지 수 세기)
    remain[arr[0]%M] += 1
    for i in range(1, N):
        arr[i] = arr[i] + arr[i-1]
        remain[arr[i] % M] += 1
    
    # 초기값 -> 나머지가 0인 개수
    ans = remain[0]

    for cnt in remain.values():
        # cnt C 2
        ans += cnt * (cnt-1) // 2
    
    # 출력
    print(ans)



if __name__ =="__main__":
    main()

```

### [영준](/나머지%20합/영준.py)

```py

```

<br/>



</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

## [환상의 짝궁 2](https://www.codetree.ai/problems/wonderful-couple2/description)

### [민웅](./환상의%20짝꿍%202/민웅.py)

```py
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
```

### [상미](./환상의%20짝꿍%202/상미.py)

```py

```

### [성구](./환상의%20짝꿍%202/성구.py)

```py
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
cards = sorted(list(map(int, input().split())))

start, end = 0, N-1
answer = "No"
while start < end:
    mid = cards[start]+cards[end]
    if mid == K:
        answer = "Yes"
        break
    elif mid > K:
        end -= 1
    else:
        start += 1

print(answer)
```

### [영준](./환상의%20짝꿍%202/영준.py)

```py

```

## [거스름돈 계산하기](https://www.codetree.ai/problems/calculating-change/description)

### [민웅](./거스름돈%20계산하기/민웅.py)

```py
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
```

### [상미](./거스름돈%20계산하기/상미.py)

```py

```

### [성구](./거스름돈%20계산하기/성구.py)

```py
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
    pirnt(-1)
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
```

### [영준](./거스름돈%20계산하기/영준.py)

```py

```

## [코드트리 테트리스](https://www.codetree.ai/problems/codetree-tetris/description)

### [민웅](./코드트리%20테트리스/민웅.py)

```py
# 코드트리 테트리스
import sys
input = sys.stdin.readline
dxy = [(1, 0), (-1, 0), (0, 1)]
extra_dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bt(x, y, score, v, l, d_lst):
    global ans
    if l == 5:
        if score > ans:
            ans = score
        return

    if score + max_value*(5 - l) <= ans:
        return

    for k in range(3):
        nx = x + dxy[k][0]
        ny = y + dxy[k][1]
        if 0 <= nx <= N-1 and 0 <= ny <= M-1:
            if not v[nx][ny]:
                if len(d_lst) >= 2:
                    if d_lst[-1] == k and d_lst[-2] == k:
                        continue
                    else:
                        v[nx][ny] = 1
                        d_lst.append(k)
                        bt(nx, ny, score + field[nx][ny], v, l + 1, d_lst)
                        d_lst.pop()
                        v[nx][ny] = 0

                else:
                    v[nx][ny] = 1
                    d_lst.append(k)
                    bt(nx, ny, score + field[nx][ny], v, l+1, d_lst)
                    d_lst.pop()
                    v[nx][ny] = 0



N, M = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]
max_value = max([max(i) for i in field])
ans = 0
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        # 반복문 안에서 방문배열을 재선언하지않는것이 중요
        visited[i][j] = 1
        # 백트래킹으로 4칸이상 연속되는 길이 제외 나머지 가능한 모든 모양 체크
        bt(i, j, field[i][j], visited, 1, [])
        visited[i][j] = 0

        # 십자가모양 체크
        cross_check = field[i][j]
        for x in range(4):
            ni = i + extra_dxy[x][0]
            nj = j + extra_dxy[x][1]
            if 0 <= ni < N and 0 <= nj < M:
                cross_check += field[ni][nj]
            else:
                break
        else:
            ans = max(ans, cross_check)

        # T자 모양 체크
        for x in range(4):
            tmp_sum = field[i][j]
            for y in range(4):
                if (x+2)%4 == y:
                    ni = i + 2*extra_dxy[y][0]
                    nj = j + 2*extra_dxy[y][1]
                    if 0 <= ni < N and 0 <= nj < M:
                        tmp_sum += field[ni][nj]
                    else:
                        break

                if x == y:
                    continue
                ni = i + extra_dxy[y][0]
                nj = j + extra_dxy[y][1]
                if 0 <= ni < N and 0 <= nj < M:
                    tmp_sum += field[ni][nj]
                else:
                    break
            else:
                ans = max(ans, tmp_sum)

        # 1 0 0
        # 1 1 1
        # 0 1 0
        # 같은 모양들 체크 -> ㅜ, ㅓ, ㅏ, ㅗ 모양에서 튀어나오지않은 방향의 양방향을 찍어서 체크
        for x in range(4):
            if extra_dxy[x][0] != 0:
                for idx in [-1, 1]:
                    tmp_sum = field[i][j]
                    ni = i + extra_dxy[x][0]
                    nj = j + extra_dxy[x][1]
                    nj = nj + idx
                    if 0 <= ni < N and 0 <= nj < M:
                        tmp_sum += field[ni][nj]
                        for y in range(4):
                            if x == y:
                                continue
                            ni = i + extra_dxy[y][0]
                            nj = j + extra_dxy[y][1]
                            if 0 <= ni < N and 0 <= nj < M:
                                tmp_sum += field[ni][nj]
                            else:
                                break
                        else:
                            ans = max(ans, tmp_sum)
                    else:
                        continue
            else:
                for idx in [-1, 1]:
                    tmp_sum = field[i][j]
                    ni = i + extra_dxy[x][0]
                    nj = j + extra_dxy[x][1]
                    ni = ni + idx
                    if 0 <= ni < N and 0 <= nj < M:
                        tmp_sum += field[ni][nj]
                        for y in range(4):
                            if x == y:
                                continue
                            ni = i + extra_dxy[y][0]
                            nj = j + extra_dxy[y][1]
                            if 0 <= ni < N and 0 <= nj < M:
                                tmp_sum += field[ni][nj]
                            else:
                                break
                        else:
                            ans = max(ans, tmp_sum)
                    else:
                        continue

print(ans)
```

### [상미](./코드트리%20테트리스/상미.py)

```py

```

### [성구](./코드트리%20테트리스/성구.py)

```py

```

### [영준](./코드트리%20테트리스/영준.py)

```py

```

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

</details>
