# 상 오 하 왼
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def make_number(start, temp):
    # DFS 로 구현해보기
    if len(temp) == 7:
        number_set.add(temp)
        return

    for direction in range(4):
        nr = start[0] + dr[direction]
        nc = start[1] + dc[direction]

        if 0 > nr or nr >= 4 or 0 > nc or nc >= 4:
            continue 
        
        make_number((nr,nc), temp+board[nr][nc])



for tc in range(1, int(input())+1):
    board = [input().split() for _ in range(4)]
    # combination 
    number_set  = set()
    for r in range(4):
        for c in range(4):
            start = (r,c)
            make_number(start, board[r][c])
    
    print('#{} {}'.format(tc, len(number_set)))