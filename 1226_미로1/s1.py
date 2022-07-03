# 목적지에 도달 가능한가 여부를 판단하면 되므로
# dfs로 문제를 푼다.

import sys

sys.stdin = open('input.txt')

def dfs(here, end):
    # here : [r, c]
    # 현재 위치 방문 체크
    maze[here[0]][here[1]] = 1

    # 현재 위치가 목적지라면 return 1 (도달 가능)
    if here == end:
        return 1

    # 델타 방식의 탐색
    # 시계방향
    # 위, 오, 아래, 왼
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 후보군
    candidate = []

    # 현재 위치를 기준으로 네 방향으로 탐색하며 현재 위치에서 갈 수 있는 후보군을 선정
    # 후보군을 각각 돌면서 재귀로 깊이 탐색

    # 갈 수 있는 곳 : 나아갈 방향의 좌표값이 미로 범위 안에 있고, 1(벽)이 아닐 때
    # 그리고 이전에 방문한 곳이 아닌 곳!
    for dir in range(4):
        r = here[0] + dr[dir]
        c = here[1] + dc[dir]

        if 0 <= r < 16 and 0 <= c < 16 and maze[r][c] != 1:
            candidate.append([r, c])

    for go in candidate:
        next_place = dfs(go, end)
        if next_place: # 다음 장소가 목적지라면?
            return 1 # 도달 가능 1 리턴('목적지!')

    # 후보군을 모두 돌았는데도 목적지가 나오지 않으면
    return 0


for tc in range(1, 11):
    test_case = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    # 시작점과 목적지 탐색
    start = []
    end = []
    for row in range(16):
        for col in range(16):
            if maze[row][col] == 2: # 시작점
                start = [row, col]
            elif maze[row][col] == 3: # 도착점
                end = [row, col]


    print('#{} {}'.format(tc, dfs(start, end)))
