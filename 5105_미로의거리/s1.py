import sys

sys.stdin = open('sample_input.txt')
tests = int(input())


def escape(here_point, end):

    queue = [] # 큐 생성
    # 현재 위치 큐에 저장
    queue.append(here_point)

    # here_point: [r, c]

    # 델타 방식의 탐색
    # 시계방향
    # 위, 오, 아래, 왼
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    visited = [[0] * N for _ in range(N)]

    # 큐가 빌 때까지 주위 인접한 노드들을 계속 탐색
    while queue:
        here = queue.pop()         # deque
        # visited[here[0]][here[1]] = 1 # 방문 체크

        for direction in range(4):
            r = here[0] + dr[direction]
            c = here[1] + dc[direction]
            # 갈수 있는 곳 : 나아갈 방향의 좌표값이 미로 범위 안에 있고, 1(벽)이 아닐 때
            # 그리고 갈 수 있는 곳이 이전에 간 곳이 아닐 때
            if 0 <= r < N and 0 <= c < N and maze[r][c] != 1:
                # 현재 위치를 기준으로 인접한 노드들 중 갈 수 있는 곳을 탐색
                # 그 중 이전에 방문했던 곳이 아니라면 queue에 저장
                if not visited[r][c]:
                    # 갈 수 있는 모든 곳을 queue에 저장
                    queue.append([r, c])
                    # 방문 거리 누적
                    # 만약 다음에 가는 공간이 목적지라면? => 현재까지 누적된 방문거리 return
                    if [r, c] == end:
                        return visited[here[0]][here[1]]
                    else:
                        visited[r][c] = visited[here[0]][here[1]] + 1
    # 목적지로 갈 수 없는 경우
    return 0

for tc in range(1, tests+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    start = []
    end = []
    # 시작점 과 끝점 찾기
    for row in range(N):
        for col in range(N):
            if maze[row][col] == 2:
                start = [row, col]
            elif maze[row][col] == 3:
                end = [row, col]

    ans = escape(start, end)
    print('#{} {}'.format(tc, ans))


'''
미로 사방에 벽을 세워서 델타 탐색 없이 단순 조건으로 푸는 방법
solution)
by 6조

import sys
sys.stdin = open('input.txt')

def calc_distance(maze, size):
    visited = [[0 for _ in range(size+1)] for _ in range(size+1)]
    queue = []

    dx = [0, 1, -1, 0]  # 상 우 좌 하
    dy = [-1, 0, 0, 1]

    # 사방으로 1값을 둘러줌
    maze = [[1 for _ in range(size)]] + maze + [[1 for _ in range(size)]]
    maze = [[1] + row + [1] for row in maze]

    # 출발지의 x, y 좌표를 찾음
    for i in range(1, size+1):
        if 2 in maze[i]:
            for j in range(1, size+1):
                if maze[i][j] == 2:
                    x = i
                    y = j
                    break

    # 도착지에 도달하지 않은 경우 반복
    while maze[x][y] != 3:
        # 현재 칸의 인접한 칸 4개에 대해 현재 칸으로부터의 거리, 방문여부 표시
        for k in range(4):
            check_x = x + dx[k]
            check_y = y + dy[k]
            if maze[check_x][check_y] != 1 and visited[check_x][check_y] == 0:
                queue.append((check_x, check_y))
                visited[check_x][check_y] = visited[x][y] + 1
        # 도착지에 다다르지 못했는데 더 이상 방문할 칸이 없을 경우 0 리턴
        if not queue:
            return 0
        # 큐에서 한 요소를 꺼내 방문할 칸으로 만듦
        x, y = queue.pop(0)

    # 지나온 칸 수를 세야하므로 도착지 칸 수를 빼고 리턴
    return visited[x][y] - 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = calc_distance(arr, N)
    print('#{} {}'.format(tc, result))



'''



