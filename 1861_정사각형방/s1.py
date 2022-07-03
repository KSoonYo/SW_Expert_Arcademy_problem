'''
시간 초과

'''


# 상 하 좌 우 

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, cnt=1):

    for direction in range(4):
        nr = r + dr[direction]
        nc = c + dc[direction]

        if 0 <= nr < N and 0 <= nc < N:
            if num[r][c] + 1 == num[nr][nc]:
                return dfs(nr, nc, cnt+1)

    return cnt
    
    




    
for tc in range(1, int(input())+1):
    N = int(input())


    num = [list(map(int, input().split())) for _ in range(N)]

    possible = [0] + list(range(1, N**2+1))
    max_cnt = 1
    memory = [987654321, max_cnt]
    for r in range(N):
        for c in range(N):
            if N == 1:
                memory = [1,1]

            if max(possible) - num[r][c] < N or max(possible) - num[r][c] + 1 < memory[1]:
                continue
            
            max_cnt = max(max_cnt, dfs(r, c))

            if memory[1] < max_cnt:
                memory = [num[r][c], max_cnt]
            
            elif memory[1] == dfs(r, c) and memory[0] > num[r][c]:
                memory[0] = num[r][c]


    print('#{}'.format(tc), *memory)
    