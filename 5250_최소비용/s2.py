
# 위, 오, 아래, 왼
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def prim(start):
    queue = [start]

    while queue:
        r,c = queue.pop(0)
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < N and 0 <= nc < N: # 현재 위치에서 갈 수 있는 다음 노드
                # 다음 위치에 가기 위해 필요한 추가 연료
                if map_info[r][c] < map_info[nr][nc]: # 다음 위치의 높이가 현재 위치의 높이보다 높다면
                    alpha = map_info[nr][nc] - map_info[r][c] # 추가 연료 계산
                else:
                    alpha = 0

                # alpha를 쉽게 설정하는 법 by 찬의님
                # alpha = max(0, map_info[nr][nc] - map_info[r][c])
                
                # 지금까지 누적된 연료 + 1(가려는 위치에 가기 위한 기본 필요 연료) + alpha(추가 필요 연료) 이
                # 가려는 위치에 이전에 기록해두었던 연료양보다 작다면
                # 최소값 갱신 + 해당 위치에 방문
                if key[r][c] + alpha + 1 < key[nr][nc]:
                    key[nr][nc] = key[r][c] + alpha + 1
                    queue.append((nr, nc)) 
            

        


for tc in range(1, int(input())+1):
    N = int(input())

    map_info = [list(map(int, input().split())) for _ in range(N)]
    start = (0,0)

    key = [[987654321] * N for _ in range(N)]
    key[0][0] = 0 # 출발지점 초기화

    prim(start)
    print('#{} {}'.format(tc, key[N-1][N-1]))
