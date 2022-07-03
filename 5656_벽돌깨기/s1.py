# 각 열의 가장 꼭대기층부터
# 완전탐색으로 벽돌을 한번씩 깨본다.(dfs - 최대 구슬 횟수 N 만큼)
# 벽돌깨기 기본 전략: 한 곳만 판다.(한 열을 선택했다면 남은 구슬 횟수를 모두 그곳에 집중한다.)
# 선택한 열이 모두 터졌다면 남은 N만큼 나머지 꼭대기를 같은 방식으로 터트려본다.

# 연쇄폭발이 가장 많이 일어나는 열을 pick(상하좌우로 벽돌 숫자 -1 이내 범위만큼 폭파)
# => 벽돌 숫자 -1 이내 범위에 있는 모든 벽돌들을 queue에 넣음
# queue가 빌 때까지 벽돌을 모조리 폭파

# N이 넘어갈 때마다 벽돌 재배치
# N=0이면 벽돌을 초기 모습으로 복구

# 기본 폭파 범위
# 왼, 오, 상, 하
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

import sys

sys.stdin = open('input.txt')

def bang(N, start, bricks_info, bump_cnt):
    global max_cnt
  
    # print('start', start)
    # 폭발처리 기록 리스트
    bump = [[0] * W for _ in range(H)]
    
    if N == 0:
        max_cnt = max(bump_cnt, max_cnt)
        return

    # 구슬 맞은 곳 폭파 처리
    bump[start[0]][start[1]] = -1
    
    queue = [start]
    bump_range_r = bump_range_c = 0

    while queue:
        now_pos = queue.pop(0)
        bump_cnt += 1
        now_weight = bricks_info[now_pos[0]][now_pos[1]]
        
        for dir in range(4): # 상 하 좌 우 네 방향 탐색
            for next_bricks in range(1, now_weight):
                bump_range_r = dr[dir] * next_bricks  
                bump_range_c = dc[dir] * next_bricks

                next_r = now_pos[0] + bump_range_r
                next_c = now_pos[1] + bump_range_c

                
                if 0 <= next_r < H and 0 <= next_c < W and (not bump[next_r][next_r]):
                    bump[next_r][next_c] = -1 # 폭파 처리
                    queue.append((next_r, next_c))
    
    # 벽돌 재배치
    # 밑에서부터 위로 올라오면서 새로 쌓기(stack)
    new_bricks_info = [[0] * W for _ in range(H)]
    for col in range(W-1, -1, -1):
        top1 = top2 = H-1 # 행의 idx
        
        
        # top1을 위로 올려보내보기
        top1 -= 1

        while top1 >= 0:
            if bricks_info[top1][col] == 0:
                break

            # 폭발하지 않은 것이 있다면
            # 아래로 내린다.
            if bump[top1][col] != -1:
                new_bricks_info[top2][col] = bricks_info[top1][col]
                top2 -= 1
    
            top1 -= 1


    # 새로운 벽돌 모양의 꼭대기 리스트
    new_top = [0] * W
    
    for row in range(H):
        for col in range(W):
            if new_bricks_info[row][col] != 0 and new_top[col] == 0:
                new_top[col] = row

    print('new top', new_top)

    for col_idx in range(W):
        if not new_top[col_idx]: # 해당 열에 구슬로 맞출 것이 아무것도 없으면 다음 열 꼭대기로 넘어감
            continue 
        bang(N-1, (new_top[col_idx], col_idx), new_bricks_info, bump_cnt)


        
for tc in range(1, int(input())+1):
    # N: 최대 구슬 쏠 수 있는 횟수
    # W : 가로 너비
    # H : 세로 너비
    N, W, H = map(int, input().split())
    

    # 벽돌 입력받기
    bricks_info = [list(map(int, input().split())) for _ in range(H)]
    
    # 각 열의 꼭대기 리스트(각 인덱스가 열, 인덱스 값은 꼭대기가 위치한 row)
    # 0번째 값이 1 => 0번째 열의 꼭대기가 위치한 행이 1번째 행
    top = [0] * W

    max_cnt = 0

    for row in range(H):
        for col in range(W):
            if bricks_info[row][col] != 0 and top[col] == 0:
                top[col] = row

    
    for col_idx in range(W):
        bang(N, (top[col_idx], col_idx), bricks_info, 0)


    # 원본 벽돌맵에서 최대 폭발한 개수를 뺀다.
    cnt = 0
    for h in range(H):
        for w in range(W):
            if bricks_info[h][w]:
                cnt += 1
    
    result = cnt - max_cnt
    print('#{} {}'.format(tc, result))



# solution
# 이 문제는 중복순열을 이용한 풀이
'''
T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(H)]
    min_value = W * H

    # 중복 순열 활용
    def rec(depth, N, now_field):
        global min_value

        if depth == N:
            # 남아있는 벽돌 갯수(최소값)
            now_value = 0
            for i in range(H):
                for j in range(W):
                    if now_field[i][j]:

                        now_value += 1

            min_value = min(now_value, min_value)        

        else:
            # 중복 순열
            for col_idx in range(W):
                # 벽돌 깨기
                new_field = [row_data[:] for row_data in now_field] # 리스트 복사
                
                # BFS 
                queue = []

                for row_idx, row_data in enumerate(new_field):
                    if row_data[col_idx]:
                        queue.append((row_idx, col_idx, row_data[col_idx]))
                        break

                while queue:
                    now_row, now_col, count = queue.pop(0)

                    # BFS 
                    # 수평(왼쪽 -> 오른쪽)
                    # now_row 변하지 않는다
                    # col이 변함
                    from_col = max(0, now_col - (count - 1)) # 왼쪽 범위
                    to_col = min(W-1, now_col + (count - 1)) # 오른쪽 범위
                    for next_col in range(from_col, to_col + 1):
                        # 수평 범위만큼 벽돌 깨기
                        if 1 < new_field[now_row][next_col]:
                            queue.append((now_row, next_col, new_field[now_row][next_col]))
                        # 벽 깨기
                        new_field[now_row][next_col] = 0

                    # 수직
                    # now_col 변하지 않음
                    from_row = max(0, now_row - (count - 1))
                    to_row = min(H-1, now_row + (count - 1)) 

                    for next_row in range(from_row, to_row + 1):
                        if 1 < new_field[next_row][next_col]:
                            queue.append((next_row, now_col, new_field[next_row][now_col]))
                        # 벽 깨기
                        new_field[next_row][now_col] = 0
                    
                # 정리
                for w in range(W):
                    real_idx = H-1
                    for h in range(H-1, -1, -1):
                        if not new_field[h][w]:
                            continue
                        new_field[real_idx][w], new_field[h][w] = new_field[h][w], new_field[real_idx][w]
                        real_idx -= 1

                rec(depth+1, N, new_field)

    rec(0, N, field)
    print()

'''
