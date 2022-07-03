
# 상 하 좌 우 

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N = int(input())

    nums = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N**2 +1) # 0, 1 ~ N^2 까지 숫자가 하나씩은 나와야 함 (문제 조건)

    for row in range(N):
        for col in range(N):
            # 현재 위치에서 사방 탐색
            here = (row, col)
            for direction in range(4):
                nr = here[0] + dr[direction]
                nc = here[1] + dc[direction]
                
                if 0 <= nr < N and 0 <= nc < N:
                    # 현재 위치에서 +1 한 값이 다음 위치에 있다면 visited[현재위치]에 표시
                    if nums[row][col] + 1 == nums[nr][nc]:
                        visited[nums[row][col]] = 1


    # visited 끝에서부터 순회
    # 0을 만나면 초기화 후 continue
    # 쌓인 cnt가 있다면
    # 시작 위치는 0을 만난 인덱스 + 1
    # 방의 개수 = cnt + 1
    cnt = 0
    room = []
    for idx in range(len(visited)-1, -1, -1):
        if not visited[idx]:
            if cnt:
                room_start = idx + 1
                room_cnt = cnt + 1
                room.append([room_start, room_cnt])
                cnt = 0
            continue

        cnt += 1

    room.sort(key=lambda x : (-x[1], x[0]))

    print('#{}'.format(tc), *room[0])