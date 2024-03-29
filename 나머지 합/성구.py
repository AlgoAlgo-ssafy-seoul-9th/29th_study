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
