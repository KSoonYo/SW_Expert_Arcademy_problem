# 윗줄에서 아랫줄로 
# 시작 방향은 오른쪽 아래
# 이후 노드 지점의 선택지는 왼쪽 아래와 오른쪽 아래(시계방향)

# 이전 방향이 오른쪽 아래 였다면 => 다음 방향은 왼쪽 아래 or 오른쪽 아래 
# 이전 방향이 왼쪽 아래 였다면 => 다음 방향은 왼쪽 위 or 왼쪽 아래 
# 이전 방향이 왼쪽 위 였다면 => 다음 방향은 왼쪽 위 or 오른쪽 위 


# 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
dr = [-1, -1, 1, 1]
dc = [-1, 1, -1, 1]

for tc in range(1, int(input())+1):
    N = int(input()) # 한 변의 길이

    cafe_info = [list(map(int, input().split())) for _ in range(N)]
    visit =  [[0] * N for _ in range(N)]
    
    def route_search(start, start_dir, end, route=[], stack=[]):
        global maxV
        

        # 목적지점에서 왼쪽 아래에 있는 지점
        pre_end = (end[0] + dr[2], end[1] + dc[2]) # 가지치기를 하자면 pre_end의 요소가 0보다 작은 경우 바로 return 하는 식으로 할 수 있을 듯
        # print('pre_end', pre_end)
        # print('start', start)
        if start == pre_end:
            if cafe_info[start[0]][start[1]] not in stack:
                maxV = max(maxV, len(stack)+1)
            return

        route.append(start) # 방문처리
        stack.append(cafe_info[start[0]][start[1]]) # 방문한 디저트 카페 종류 stack + 1

        next_r = start[0] + dr[start_dir]
        next_c = start[1] + dc[start_dir]

        # print('route', route)
        # 다음에 갈 수 있는 방향과 노드 탐색
        if 0 <= next_r < N and 0 <= next_c < N and ((next_r, next_c) not in route) and (cafe_info[next_r][next_c] not in stack):
            next_node = (next_r, next_c)
            # print('next node', next_node)
          
            if start_dir == 3:
                route_search(next_node, 2, end, route, stack)
                route_search(next_node, 3, end, route, stack)
            elif start_dir == 2:
                route_search(next_node, 0, end, route, stack)
                route_search(next_node, 2, end, route, stack)
            elif start_dir == 1:
                route_search(next_node, 1, end, route, stack)
            elif start_dir == 0:
                route_search(next_node, 0, end, route, stack)
                route_search(next_node, 1, end, route, stack)
            

        route.pop()
        stack.pop()
        
    maxV = -1

    for row in range(N):
        for col in range(N):
            route_search((row, col), 3, (row, col))

    print('#{} {}'.format(tc, maxV))



'''
solution) by 3조

방향을 아름답게 꺾는법
어차피 사각형을 그리려면, 현재 노드에서는 이전 방향과 같은 방향으로 가거나 꺾어서 다른 방향으로 가는 방법 2가지 경우가 존재
2가지 경우에 대한 조건만 잘 걸어주면 코드를 간략하게 짤 수 있다.

시계방향으로 사각형 그리기

```python
have_eaten = []
dir_his = set([])

def is_safe(i, j):
    if -1 < i < N and -1 < j < N:  # idx가 범위 안에 있고
        if field[i][j] in have_eaten:  # 먹어봤으면 False
            return False

        if not visited[i][j]:  # 방문 안했으면 True
            return True
    return False  # idx가 범위를 넘어가면 False

def search(a, b, prev):
    global can_eat
    if [a, b] == start and len(have_eaten) > 3:  # 출발점이고, 먹어본 디저트가 3개보다 크면
        can_eat = max(can_eat, len(have_eaten))  # 먹을 수 있는 디저트, 먹어본 디저트 중 큰걸로
        return
    
    # 방향 x, y
    dirs = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

    # 방향을 틀면 기존에 가던 방향으로는 못간다
    for dy, dx in dirs:
        if (dy, dx) not in dir_his:      # 진행한 방향이 아니면
            n_y = a + dy                 # 새로운 행 좌표
            n_x = b + dx                 # 새로운 열 좌표
            if is_safe(n_y, n_x):        # 유효하면
                visited[n_y][n_x] = 1    # visited 2차원 배열에 방문 처리
                have_eaten.append(field[n_y][n_x])  # 디저트 종류를 stack에 append
                if prev != (dy, dx):                # 이전 방향과 다르다면
                    dir_his.add(prev)               # 가본 거에 이전 방향 추가해서 다신 안가게
                    search(n_y, n_x, (dy, dx))      # 새 방향으로 search 진행
                    dir_his.remove(prev)            # 끝까지 갔다가 올라올 때 가본 방향 삭제
                else:  # 이전 방향이 같다면 같은 방향으로 이어서 search 진행
                    search(n_y, n_x, prev)

                visited[n_y][n_x] = 0    # 끝까지 갔다가 올라올 때 visited한 곳 삭제
                have_eaten.pop()         # 먹어본 것 삭제

T = int(input())
for test_case in range(1, T + 1):
    can_eat = 0  # 먹을 수 있는 최대 디저트 개수
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    # 출발점
    for a in range(N):
        for b in range(N):
            start = [a, b]
            search(a, b, (1, 1))

    if can_eat == 0:
        can_eat = -1
    print('#{} {}'.format(test_case, can_eat))
```
    
    

'''
