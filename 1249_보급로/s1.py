from collections import deque

'''
일반 queue로 푸니까 안되는데, deque로 하니까 된다...
list로 만든 queue의 시간복잡도는 O(n)
deque 는 무려 O(1) !!!!
'''

for tc in range(1, int(input())+1):
    N = int(input())

    map_info = [list(input()) for _ in range(N)]

    idx = 0
    for row in map_info:
        map_info[idx] = list(map(int, row))
        idx += 1

    visited = [[float('INF')] * N for _ in range(N)] # 최소 cost 업데이트를 위한 방문 리스트
    
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우 방향

    start_right = (0, 1)
    cost_right = map_info[0][1]
    
    start_down = (1, 0)
    cost_down = map_info[1][0]
    
    queue = deque()
    queue.append((start_right, cost_right))
    queue.append((start_down, cost_down))
    
    visited[start_right[0]][start_right[1]] = cost_right
    visited[start_down[0]][start_down[1]] = cost_down
    
   
    while queue:
        
        here, cost = queue.popleft()

        # 사방탐색
        # 지금까지 누적한 cost에서 다음 위치의 cost를 더한 값 구하기(map_info로)
        # 더한 값과 다음위치의 visited 값을 비교 => 더한 값이 현재 visited값보다 작으면 
        # => visited값 갱신, 다음 위치를 queue에 append

        for direction in directions:
            nr = here[0] + direction[0]
            nc = here[1] + direction[1]

            if 0 <= nr < N and 0 <= nc < N and (nr, nc) != (0,0):
                next_cost = cost + map_info[nr][nc]
                if visited[nr][nc] > next_cost and visited[N-1][N-1] > next_cost:
                    visited[nr][nc] = next_cost
                    queue.append(((nr, nc), next_cost))

       
    print('#{} {}'.format(tc, visited[N-1][N-1]))