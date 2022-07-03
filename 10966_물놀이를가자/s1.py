

for tc in range(1, int(input())+1):
    # N개의 줄
    # 길이 M 문자열
    N, M = map(int, input().split())
    
    # flood fill 기법으로 풀이(BFS) 물 => 땅까지의 거리
    # 땅 자리에 있는 칸에 물에서 땅까지의 거리를 넣는다.
    visited = [[0] * M for _ in range(N)]

    # 물이 있는 곳을 시작지점으로
    queue = [] 
    front = rear = -1
    pool = [0] * N

    # 수영장 입력받으면서 시작점 찾기
    # 입력 규모가 크다면 굳이 수영장 입력받고 수영장을 전부 탐색할 필요 없이
    # 이렇게 입력받으면서 시작점을 찾는 방법도 실행시간 단축에 도움이 될 수 있다.
    for row_idx in range(N):
        temp = input()
        for col_idx in range(M):
            if temp[col_idx] == 'W':
                queue.append((row_idx, col_idx))
                rear += 1
        pool[row_idx] = temp


    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상 하 좌 우
    distance_total = 0
    while front != rear:
        front += 1
        now_r, now_c = queue[front]
        # 사방 탐색
        for direction in directions:
            next_r = now_r + direction[0]
            next_c = now_c + direction[1]

            if 0 <= next_r < N and 0 <= next_c < M:
                if not visited[next_r][next_c] and pool[next_r][next_c] != 'W':
                    queue.append((next_r, next_c))
                    rear += 1
                    visited[next_r][next_c] = visited[now_r][now_c] + 1
                    distance_total += visited[next_r][next_c]

    print('#{} {}'.format(tc, distance_total))
    
