
# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def route_search(start, k, cnt=1, length=1):
    '''
    start : 시작 지점
    k : 최대 깎을 수 있는 깊이(1~K)
    cnt: 최대 깎을 수 있는 횟수
    '''

    global max_length
    # 현재 위치 방문처리
    visited[start[0]][start[1]] = 1
    max_length = max(length, max_length)


    # 현재 위치에서 다음 갈 수 있는 노드 탐색
    # 다음 노드의 높이를 깎는 경우와 깎지 않을 경우를 탐색해야 함
    for dir in range(4):
        nr = start[0] + dr[dir]
        nc = start[1] + dc[dir]

        if 0 <= nr < N and 0 <= nc < N:
            if (not visited[nr][nc]):
                # 깎는 경우: cnt가 1이고 다음 방문할 노드의 높이가 현재 노드의 높이보다 크거나 같을 때
                if cnt and mountain_map[nr][nc] >= mountain_map[start[0]][start[1]]:
                    # 현재 높이 - 1 만큼 깎을 수 있는 지 검증
                    if mountain_map[start[0]][start[1]] - 1 >= mountain_map[nr][nc] - k:
                        # 깎을 수 있다면   
                        # 다음 노드의 높이는 현재 높이 - 1
                        original_next_height = mountain_map[nr][nc]
                        mountain_map[nr][nc] = mountain_map[start[0]][start[1]] - 1
                        route_search((nr,nc), k, 0, length+1) # 깎고 나서는 다시 복구
                        mountain_map[nr][nc] = original_next_height

                # 깎지 않는 경우: 다음 방문할 노드의 높이가 현재 노도의 높이보다 작을 때
                if mountain_map[nr][nc] < mountain_map[start[0]][start[1]]:
                    route_search((nr, nc), k, cnt, length+1)
    
    # 현재 위치 방문 초기화
    visited[start[0]][start[1]] = 0
  




for tc in range(1, int(input())+1):
    N, K = map(int, input().split()) # N: 한 변의 길이 / K: 최대 공사 가능 깊이
    
    mountain_map = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 봉우리 지점 탐색
    top_height = 0
    top_point = []
    for row in range(N):
        top_height = max(top_height, max(mountain_map[row]))

    for r in range(N):
        for c in range(N):
            if mountain_map[r][c] == top_height:
                top_point.append((r,c))

    max_length = 0
    for start in top_point:
        visited = [[0] * N for _ in range(N)]
        route_search(start, K)

    print('#{} {}'.format(tc, max_length))
