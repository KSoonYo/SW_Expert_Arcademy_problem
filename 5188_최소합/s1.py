
# dfs로 풀어보기
####
# Runtime error 발생 => 가지치기 필요
####

# 오 아래
dr = [0, 1]
dc = [1, 0]

def dfs(here_point, end, total, min_v):
    total += num_list[here_point[0]][here_point[1]] 

    if total > min_v: # 가지치기
        return min_v

    if here_point == end:
        min_v = min(total, min_v)
        return min_v
    
    candidates = []
    for next in range(2):
        next_r = here_point[0] + dr[next]
        next_c = here_point[1] + dc[next]

        if next_r < N and next_c < N and (not visited[next_r][next_c]):
            visited[next_r][next_c] = 1
            candidates.append((next_r, next_c))
    
    for next_point in candidates:
        min_v = dfs((next_point[0], next_point[1]), end, total, min_v)
        visited[next_point[0]][next_point[1]] = 0

    return min_v


for tc in range(1, int(input())+1):
    # 가로 세로 칸 수
    N = int(input())

    # 배열 입력
    num_list = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    
    start = (0,0)
    end = (N-1, N-1)
    max_values = list(map(max, num_list)) 
    min_v = max(max_values) ** 2
    result = dfs(start, end, 0, min_v)

    print('#{} {}'.format(tc, result))



'''
solution 
list slicing 으로 순열 구하기

```python
import sys
sys.stdin = open('input.txt')

def calc_battery(amount, row, remaining_c):
    global min_v

    # remaining_c 리스트가 비었다면 = 남은 컬럼이 0뿐이라면
    if not remaining_c:
        amount += arr[row][0]
        if amount < min_v:
            min_v = amount
        return

    for i in range(len(remaining_c)):
        col = remaining_c[i]
        # row == col 일 때 해당 위치 값은 0이니까 continue
        if row == col:
            continue
        # arr[1][2] 다음엔 arr[2][?] 방문해야 하므로 col이 row가 됨
        calc_battery(amount + arr[row][col], col, remaining_c[:i] + remaining_c[i+1:])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 100 * N     # 한 칸의 최댓값 100
    # 사무실에서 출발하므로 row는 0부터 시작
    # 마지막에 (row, 0) 방문하기 위해 컬럼 리스트는 1부터 시작
    calc_battery(0, 0, [num for num in range(1, N)])

    print('#{} {}'.format(tc, min_v))
```

'''