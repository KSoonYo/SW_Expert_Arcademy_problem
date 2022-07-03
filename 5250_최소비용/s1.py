

'''
dfs 풀이 
=> runtime error
'''

# 위, 오, 아래, 왼
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(start, end, now_height, fuel=0):
    global min_fuel

    if fuel > min_fuel:
        return

    if start == end:
        min_fuel = min(min_fuel, fuel)
        return

    # 현재 위치 방문 처리
    visited[start[0]][start[1]] = 1
    
    next_nodes = []

    for dir in range(4):
        nr = start[0] + dr[dir]
        nc = start[1] + dc[dir]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            next_nodes.append((nr, nc))

    for next_node in next_nodes:
        alpha = 0
        next_height = map[next_node[0]][next_node[1]]
        if now_height < next_height:
            alpha = next_height - now_height
        
        dfs(next_node, end, next_height, fuel+1+alpha)
    
    visited[start[0]][start[1]] = 0 # 방문 초기화
    


for tc in range(1, int(input())+1):
    N = int(input())

    map = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [[0] * N for _ in range(N)]
    start = (0,0)
    end = (N-1, N-1)

    min_fuel = 987654321
    dfs(start, end, map[start[0]][start[1]])
    
    print('#{} {}'.format(tc, min_fuel))

