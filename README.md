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

## [환상의 짝궁 2]()

### [민웅](./환상의%20짝꿍%202/민웅.py)

```py

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

## [거스름돈 계산하기]()

### [민웅](./거스름돈%20계산하기/민웅.py)

```py

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

## [코드트리 테트리스]()

### [민웅](./코드트리%20테트리스/민웅.py)

```py

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
