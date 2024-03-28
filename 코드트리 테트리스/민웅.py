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