# 상 오 하 왼
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def make_number(start):
    temp = str(board[start[0]][start[1]])
    movement = 6
    queue = [(start, movement, temp)]
    front = -1
    rear = 0
    while front != rear:
        front += 1
        here, now_movement, now_temp = queue[front]

        if now_movement < 0 and now_temp not in number_set:
            number_set.add(now_temp)
            continue

        # 사방 탐색
        for direction in range(4):
            nr = here[0] + dr[direction]
            nc = here[1] + dc[direction]

            if 0 <= nr < 4 and 0 <= nc < 4:
                next = (nr, nc)
                next_movement = now_movement - 1
                next_temp = now_temp + str(board[nr][nc])
                queue.append((next, next_movement, next_temp))
                rear += 1

            



for tc in range(1, int(input())+1):
    board = [list(input().split()) for _ in range(4)]
    # visited = [[0] * 4 for _ in range(4)]
    movemnet = 6
    # combination 
    # 총 이동 횟수는 6
    number_set  = set()
    for r in range(4):
        for c in range(4):
            start = (r,c)
            make_number(start)
    
    print('#{} {}'.format(tc, len(number_set)))