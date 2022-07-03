
tests = int(input())

def escape(here_point, n):
    # 현재 위치 방문 체크
    maze[here_point[0]][here_point[1]] = 1

    # print('here_point: ', here_point)
    flag = 0
    if here_point == end_point:
        flag = 1
        return flag

    # 네 방향 탐색을 위한 델타
    # 위 오 아래 왼
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 현재 위치
    x = here_point[0]
    y = here_point[1]

    candidate = []
    # 현재 위치에서 네 방향으로 탐색하여 범위 이내이고 벽이 아닌 장소 탐색
    # 갈 수 있는 후보군으로 지정
    for idx in range(4):
        di = x + dx[idx]
        dj = y + dy[idx]
        if 0 <= di < N and 0 <= dj < N and maze[di][dj] != 1:
            candidate.append([di, dj])

    # 갈 수 있는 후보군을 하나씩 방문
    # 후보군에서 더 갈 수 있는 곳이 있는지 재귀로 체크
    # 해당 방향에서 목적지가 나오지 않고, 더 갈 수 있는 범위가 없다면 다시 원래 지점으로 back
    for go in candidate:
        flag = escape(go, n)
        if flag:
            break

    # 갈 수 있는 후보군을 모두 돌았는데도 목적지에 도착하지 못한다면 0 리턴
    return flag


for tc in range(1, tests+1):
    N = int(input())
    maze = [[] for _ in range(N)]

    for maze_row_elem in range(N):
        maze_row = input()
        for maze_col_elem in maze_row:
            maze[maze_row_elem].append(int(maze_col_elem))
    start_point = []
    end_point = []

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 3:
                end_point.append(r)
                end_point.append(c)
            if maze[r][c] == 2:
                start_point.append(r)
                start_point.append(c)
            # 2와 3이 없는 경우도 유의!

    ans = escape(start_point, N)
    print('#{} {}'.format(tc, ans))

'''
반복문으로 구현한 dfs solution

import sys
sys.stdin = open('input.txt')

# 입력값 받아오기
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    i = 0                                                   # 현재 i 좌표
    j = 0                                                   # 현재 j 좌표
    visited = [[0] * N for _ in range(N)]                   # 방문 여부를 표시할 배열
    stack = []
    result = 0
    di = [-1, 0, 1, 0]                                      # 상 우 하 좌 탐색
    dj = [0, 1, 0, -1]                                      

    for r in range(N):          # 시작점이 있는 위치를 탐색하여 i, j 에 저장
        for c in range(N):
            if arr[r][c] == 2:
                i = r
                j = c

    stack.append([i, j])        # 시작점 스택에 push

    while stack:
        i, j = stack.pop()      # 스택의 마지막 지점을 현위치로 받아옴
        visited[i][j] = 1       # 현위치 방문 표시

        if arr[i][j] == 3:      # 현위치가 goal 이면
            result = 1          # result 에 1 을 저장하고 break
            break

        # 다음 이동 방향이 인덱스 내에 있고, 통로 또는 도착지이고, 방문한 적이 없는 곳이면 스택에 추가
        for idx in range(4):
            if (0 <= i + di[idx] < N) and (0 <= j + dj[idx] < N) and (arr[i + di[idx]][j + dj[idx]] in [0, 3]) and (visited[i + di[idx]][j + dj[idx]] == 0):
                stack.append([i + di[idx], j + dj[idx]])

    print('#{} {}'.format(test_case, result))
by 알고리즘 3주차 1조 노션 코드

'''


'''
미로 주위에 벽 세워서 푸는 방법)

# 4875 미로
T = int(input())

for _ in range(T):
    N = int(input())
    maze = [[1]+list(map(int, input()))+[1] for i in range(N)]
    maze = [[1]*(N+2)] + maze + [[1]*(N+2)] # 미로 주변에 벽(1)을 추가해 진행을 못하도록 하기 위함

    # 출발점 찾기
    for i in range(N+2):
        for j in range(N+2):
            if maze[i][j] == 2:
                me = [i, j]

    stack = [] + [me]
    visited = []

    while True:
        # 방문지 체크
        visited.append(me)

        # 도착
        if maze[me[0]][me[1]] == 3:
            result = 1
            break
        # 길 찾기
        # 방문했던 곳이 아니고 찾아낸 길이면(1을 제외한 곳) 스택에 쌓기
        if maze[me[0]+1][me[1]] != 1 and ([me[0]+1, me[1]] not in visited):
            stack.append([me[0] + 1, me[1]])
        if maze[me[0]-1][me[1]] != 1 and ([me[0]-1, me[1]] not in visited):
            stack.append([me[0] - 1, me[1]])
        if maze[me[0]][me[1]+1] != 1 and ([me[0], me[1]+1] not in visited):
            stack.append([me[0], me[1]+1])
        if maze[me[0]][me[1]-1] != 1 and ([me[0], me[1]-1] not in visited):
            stack.append([me[0], me[1]-1])

        # 길이 없어서 목적지에 도착할 수 없을 때
        if len(stack) == 0:
            result = 0
            break

        # 찾아낸 길 중 스택의 마지막 좌표로 이동 후 현 위치 변경
        me = stack.pop()

    print('#{} {}'.format(_+1, result))
by 알고리즘 3주차 6조 노션 코드
'''


