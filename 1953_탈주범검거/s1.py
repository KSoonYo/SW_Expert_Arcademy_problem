# import sys

# sys.stdin = open('input.txt')

pip_lines = {
    1 : [[-1, 0], [1, 0], [0, -1], [0, 1]],
    2 : [[-1, 0], [1, 0]],
    3 : [[0, -1], [0, 1]],
    4 : [[-1, 0], [0, 1]],
    5 : [[1, 0], [0, 1]],
    6 : [[1, 0], [0, -1]],
    7 : [[-1, 0], [0, -1]]
}

for tc in range(1, int(input())+1):
    # N, M : 세로. 가로 크기
    # R, C : 시작 세로 위치, 가로 위치
    # L : 소요된 시간   
    N, M, R, C, L  = map(int, input().split())


    map_info = [list(map(int, input().split())) for _ in range(N)]
    # print(map_info)

    start = (R, C) # 시작 지점
    queue = [(start, L-1)]
    visited = [[0] * M for _ in range(N)]
    visited[start[0]][start[1]] = 1
    cnt = 1
    while queue:
        here, now_time = queue.pop(0)
        # print('here', here)
   

        if now_time == 0:
            continue
        

        # 다음 갈 수 있는 파이프 탐색
        now_pipe = map_info[here[0]][here[1]]
        
        for next_pipes in pip_lines.get(now_pipe):
            nr = here[0] + next_pipes[0]
            nc = here[1] + next_pipes[1]

            if 0 <= nr < N and 0 <= nc < M and map_info[nr][nc]:
                if not visited[nr][nc]:
                    # 다음에 있는 파이프라인에서도 이전 파이프라인과 이어져 있는지 check
                    check = False
                    next_pipe = map_info[nr][nc]
                    
                    for before_pipe in pip_lines.get(next_pipe):
                        r = nr + before_pipe[0]
                        c = nc + before_pipe[1]

                        if r == here[0] and c == here[1]:
                            check = True
                            break

                    if check:
                        # print('next_pipe', (nr, nc))
                        visited[nr][nc] = 1 # 방문 처리
                        cnt += 1
                        queue.append(((nr, nc), now_time-1))

    print('#{} {}'.format(tc, cnt))
