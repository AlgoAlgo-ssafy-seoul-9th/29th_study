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