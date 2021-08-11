# 델타 탐색을 이용한 풀이
# 오른쪽부터 시계방향 순
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# i, j 는 이전칸
# ni, nj 는 값을 쓸 칸

T= int(input())
for tc in range(1, T+1):
    N = int(input())

    # N x N 으로 채워진 배열
    arr = [[0] * N for _ in range(N)]
    cnt = 1
    dir = 0 # 이동 방향
    i, j = 0, -1
    while cnt <= N * N: # 쓸 값이 칸 수를 넘어가지 않았으면 반복
        ni, nj = i + di[dir], j + dj[dir] # 이전칸으로 부터 진행 방향으로 이동한 칸 좌표
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0: # 영역 내부이고 아직 기록되지 않은 칸이라면
            arr[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj # 현재 칸을 다음 칸 계산을 위한 값으로 사용

        # 영역에서 벗어나거나 값이 쓰인 곳에 도달할 경우!
        else:
            # 방향 전환
            # 4가지 방향을 전환하려면 dir 값은 0 1 2 3 으로 고정되어야 함.
            # 따라서 왼쪽 방향(dir == 3) 을 하고 나서는 나머지 연산을 통해 dir을 다시 0부터 시작하게 함
            dir = (dir + 1) % 4

    # 출력
    # *를 활용한 리스트 요소 출력
    for i in range(N):
        print(*arr[i])


